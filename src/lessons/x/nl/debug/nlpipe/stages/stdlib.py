import re
import concurrent.futures

from pathlib import Path

from nlpipe.utils import named_in, named_out


def val_iter(val):
    return (val,)


def val_gen(val):
    yield val


def val_gen(val):
    yield val


def list_gen(lst):
    for elem in lst:
        yield elem


def file_to_text(gen):
    for filename in gen:
        with open(filename, 'r') as f:
            yield Path(filename).stem, f.read()


def file_lines_to_text(gen):
    for filename in gen:
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                yield (Path(filename).stem+"_"+str(i), line)


def dir_files(gen):
    return _dir_gen(gen, lambda path: path.iterdir())


def recursive_dir_files(gen):
    return _dir_gen(gen, lambda path: path.rglob('*'))


def _dir_gen(gen, path_gen_func):
    for dirname in gen:
        dir_path = Path(dirname)
        if not dir_path.is_dir():
            break
        # yield is done implicitly within the generator
        return (dir_elem for dir_elem in path_gen_func(dir_path)
                if dir_elem.is_file())

def multi_process_stages(gen, stages, workers, batch_size):
    return _parallelize(concurrent.futures.ProcessPoolExecutor,
                        gen, stages, workers, batch_size)

def multi_thread_stages(gen, stages, workers, batch_size):
    return _parallelize(concurrent.futures.ThreadPoolExecutor,
                        gen, stages, workers, batch_size)

def _parallelize(executor_type, gen, stages, workers, batch_size):

    with executor_type(max_workers=workers) as executor:

        futures_list = list()
        elems = list()

        for i, elem in enumerate(gen):
            elems.append(elem)
            if (i+1)%batch_size == 0:
                futures_list.append(executor.submit(_wind_apply_unwind, elems, stages))
                elems = list()

        futures_list.append(executor.submit(_wind_apply_unwind, elems, stages))
        elems = list()

        for future in concurrent.futures.as_completed(futures_list):
            for elem in future.result():
                yield elem

def _wind_apply_unwind(elem, stages):
    # things we can't pickle:
    ## locals (can't return a wrapper with functions or partial function)
    ## generators (can't return a generator, must unwind)

    elem = (dummy for dummy in elem) # wind element
    for stage in stages: # apply stages
        elem = stage(elem)
    return [*elem] # unwind element


def join_tokens(gen):
    for tok_list in gen:
        name, tok_list = named_in(tok_list)
        tok_list = ' '.join(tok_list)
        yield named_out(name, tok_list)


def restore_punct(gen):
    for tok_list in gen:
        name, tok_list = named_in(tok_list)
        # Remove space from before and after certain punctuation
        tok_list = re.sub(r"\s([,\.\)\]\?\!\%])", r"\g<1>", tok_list)
        tok_list = re.sub(r"([\(\[\$])\s", r"\g<1>", tok_list)
        yield named_out(name, tok_list)


def lower_text(gen):
    for text in gen:
        name, text = named_in(text)
        text = text.lower()
        yield named_out(name, text)


def rm_pattern(gen, pattern):
    for text in gen:
        name, text = named_in(text)
        text = re.sub(pattern, '', text)
        yield named_out(name, text)
