from time import time
from tqdm import tqdm
from pathlib import Path

from nlpipe.stages.stdlib import dir_files, val_gen


def print_logger(gen, tot_len='?'):
    for i, elem in enumerate(gen):
        print(f"\r{i+1}/{tot_len}", end='')
        yield elem


def tqdm_logger(gen, tot_len=None):
    start = time()
    for i, elem in enumerate(gen):
        print('\r'+tqdm.format_meter(i+1, tot_len, time()-start), end='')
        yield elem


def dir_files_tqdm_logger(gen):
    for dirname in gen:
        dir_path = Path(dirname)
        if not dir_path.is_dir():
            break
        n_files = len([name for name in dir_path.iter if Path(name).is_file()])
        for elem in tqdm_logger(dir_files(val_gen(dirname)), tot_len=n_files):
            yield elem
