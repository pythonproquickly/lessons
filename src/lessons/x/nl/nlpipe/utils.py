from inspect import signature, _empty
import numpy as np


class DummyIO:
    def close(self):
        pass


def vec_len(vec):
    return np.sqrt(np.sum(vec**2))


def opt_tokenize(func):
    func_params = signature(func).parameters
    if list(func_params.keys())[1] != "sentences":
        raise ValueError("opt_tokenize decorated functions should have their "
                         "first argument be named 'sentences'")
    if "tokenize" not in func_params or func_params["tokenize"].default == _empty:
        raise ValueError("opt_tokenize decorated functions should have a "
                         "keyword argument named 'tokenize'")

    def wrapper(self, sentences, *args, tokenize=func_params["tokenize"].default, **kwargs):
        if tokenize:
            sentences = ((doc, self.tokenizer(sentence))
                        for doc, sentence in sentences)
        return func(self, sentences, *args, tokenize=False, **kwargs)

    return wrapper


def named_in(elem):
    return elem if isinstance(elem, tuple) else (None, elem)


def named_out(name, elem):
    return name, elem if elem is not None else elem
