import nltk
from nltk.stem import WordNetLemmatizer

from nlpipe.utils import named_in, named_out


def nltk_tokenizer(gen):
    for text in gen:
        name, text = named_in(text)
        text = nltk.word_tokenize(text)
        yield named_out(name, text)


def nltk_lemmatizer(gen, *args, **kwargs):
    lemmatizer = WordNetLemmatizer(*args, **kwargs)
    for tok_list in gen:
        name, tok_list = named_in(tok_list)
        tok_list = [lemmatizer.lemmatize(tok) for tok in tok_list]
        yield named_out(name, tok_list)


def nltk_pos_tagger(gen):
    for tok_list in gen:
        name, tok_list = named_in(tok_list)
        tok_list = nltk.pos_tag(tok_list)
        yield named_out(name, tok_list)


def nltk_ner_sub(gen):
    for tok_list in gen:
        name, tok_list = named_in(tok_list)
        ret = []
        for chunk in nltk.ne_chunk(tok_list):
            if hasattr(chunk, "label"):
                ret.append(chunk.label())
            else:
                ret.append(chunk[0])
        yield named_out(name, ret)
