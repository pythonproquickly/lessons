import sys
sys.path.insert(1, "..")

import re
from pathlib import Path

from transformers import BertTokenizer, BertForSequenceClassification

from nlpipe.pipeline.gensim_pipeline import Word2VecPipeline
#from nlpipe.pipeline.huggingface_pipeline import HuggingFacePipeline

from nlpipe.stages.logging import tqdm_logger
from nlpipe.stages.stdlib import dir_files, file_to_text, join_tokens, \
                                   val_gen, named_in, named_out
from nlpipe.stages.nltk import nltk_tokenizer, nltk_lemmatizer, nltk_pos_tagger, nltk_ner_sub


def gen_paths(gen):
    """Generate required paths lazily"""

    for root_path in gen:
        # Check all files (with any level of nesting) in the specified folder.
        for path in Path(root_path).glob("**/*.txt"):
            # Path must be poinint to a file, not a directory.
            if path.is_file():
                # Split name on the string "_edgar_data_"
                cik_id = path.stem.split("_edgar_data_")
                if len(cik_id) >= 2:
                    # Check that the file is a 10-k
                    if cik_id[0].split("-")[-1].lower() == 'k':
                        yield path


def file_to_tokens(gen):
    for root_path in gen:
        for path in Path(root_path).rglob("*.txt"):
            txt = (path
                   .read_text()[1:-1]
                   .replace("'", '')
                   .replace(", ", ' '))
            # name = re.findall("_(\d+)-", path.stem)
            name = path.stem
            # if len(name) > 0:
            #     name = name[0] 
            # else:
            #     continue
        
            yield name, txt

tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
def to_bert_tokens(gen):
    for txt in gen:
        name, txt = named_in(txt)
        tok_lst = tokenizer.tokenize(txt)
        yield named_out(name, tok_lst)


if __name__ == "__main__":

    process_new = True

    workers = 2

    save_dir = Path("saved_models")
    if not save_dir.exists():
        save_dir.mkdir()

    input_dir = "all_data"

    tfidf_config= {
        "stop_words": "english"
    }
    model_config= {
        "workers": workers,
    }

    if process_new:
        dict_emb = Word2VecPipeline(source_gen=val_gen(input_dir),
                                        tfidf_config=tfidf_config)
        tot_len = len([*Path(input_dir).rglob('*.txt')])
        dict_emb.add_stage(file_to_tokens)\
                .add_stage(to_bert_tokens)\
                .add_stage(join_tokens)\
                .add_stage(tqdm_logger, stage_opts={"tot_len": tot_len})
        print("PROCESSING SOURCE")
        dict_emb.process_source()
    else:
        source = val_gen("processed_source")
        dict_emb = Word2VecPipeline(source_gen=source,
                                       tfidf_config=tfidf_config)
        dict_emb.add_stage(dir_files)
        dict_emb.add_stage(file_to_text)

    print("TRAINING TFIDF")
    dict_emb.train_tfidf(save=save_dir.joinpath("tfidf.pkl"))

    if save_dir:
        dict_emb.source_gen = None
        dict_emb.save(name=save_dir.joinpath("bert_emb.pkl"))

    print("DONE")