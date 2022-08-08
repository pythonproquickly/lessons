import sys
sys.path.insert(1, "..")

from collections import OrderedDict, defaultdict

import numpy as np
import pandas as pd

from joblib import load, dump
from pathlib import Path


from transformers import BertTokenizer, BertForSequenceClassification
from nltk.stem import WordNetLemmatizer

from nlpipe.pipeline.huggingface_pipeline import HuggingFacePipeline
from nlpipe.pipeline.gensim_pipeline import Word2VecPipeline

from nlpipe.stages.stdlib import val_iter


if __name__ == "__main__":

    input_dir = "data"
    save_dir = Path("saved_models")
    source = val_iter("processed_source")
    # seed_words = { # For testing purposes
    #     "mobile": ["mobile", "internet"],
    #     "heaters": ["heaters", "water"],
    #     "this": ["this", "is"],
    #     "asdffds": ["dsafsdfasd", "morning", "dsf"],
    #     "kjhasdf": ["lkjhasdf", "ljkha"],
    # }
    # seed_words = {
    #     "operation": ["restructure", "reorganization", "reorganize",
    #                    "reorganized", "reorganizing", "turnaround", "restructuring"],
    #     "financial": ["new_loan", "interest_concession", "debt_equity_swap", "debt_forgiveness",
    #                   "moratorium_loan_principle", "moratorium_interst_payment"],
    # }
    seed_words = {
        "Financial": ["default", "indebtedness", "downgrade",
                      "rating", "renegotiation"],
        "Operation": ["downsize", "asset", "cost","expanding",],
        "Idiosyncratic": ["idiosyncratic", "intangible", "goodwill", "franchise",
                      "weather","trade","technology"],
        "Legal": ["litigtion", "enforcement", "fines",
                      "regulatory"],
        "Systematic": ["shock","crisis","price","war","exchange","competition"],
        "sustainability": ["natural","hazard","oil","pollution","emission",
                        "chemical"],
       
    }
    lemmatizer = WordNetLemmatizer()
    seed_words = {word: [lemmatizer.lemmatize(sw) for sw in seeds]
                  for word, seeds in seed_words.items()}

    finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
    tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

    bert_emb = load(save_dir.joinpath("bert_emb.pkl"))
    bert_emb.seed_words = seed_words
    bert_emb.tokenizer = tokenizer
    bert_emb.extract_emb_weights(finbert)

    word_dict = bert_emb.get_word_dict(n=100)
    pd.DataFrame(word_dict).to_csv("dictionary.txt", index=False)
    word_to_col = bert_emb.tfidf.vocabulary_
    tfidf_res = bert_emb.tfidf_res

    word_scores = np.zeros((tfidf_res.shape[0], len(word_dict)))
    word_order = list() # as word_dict is not ordered
    for i, (word, entries) in enumerate(word_dict.items()):
        ids = [word_to_col[entry] for entry in entries if entry in word_to_col]
        word_scores[:, i] = np.squeeze(np.asarray(tfidf_res[:, ids].mean(axis=1)))
        word_order.append(word)

    company_scores = list()
    for doc_name, idx in bert_emb.doc_names.items():
        # c_id = int(doc_name)
        c_id = doc_name
        t_score = word_scores[idx]
        company_scores.append([c_id, *t_score])

    score_df = pd.DataFrame(company_scores, columns=["document_id", *word_order])
    dump(score_df, save_dir.joinpath(type(bert_emb).__name__+"_scores.pkl"))
    score_df.to_csv("scores.csv", index=False)

    print("DONE")
