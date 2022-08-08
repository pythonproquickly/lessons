from collections import OrderedDict
from functools import partial
from pathlib import Path
from joblib import dump

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

from nlpipe.utils import vec_len
from nlpipe.stages.stdlib import list_gen, file_to_text, multi_process_stages


class _ParallelIndicator:
    def __call__(self):
        raise NotImplementedError("_ParallelIndicators should not be called")


class StartParallel(_ParallelIndicator):
    """Idea: Make this a multiprocessing.Process or multiprocessing.BaseManager
    that can simply take in a set of stages, have input/output pipes and custom
    setups for subclasses (for example, setting up an stanza.nlp processor).
    """
    pass


class EndParallel(_ParallelIndicator):
    def __init__(self, workers, batch_size):
        super().__init__()
        self.workers = workers
        self.batch_size = batch_size


class _Pipeline:
    """Pipelines should start with a function that takes in some source item
    and returns an iterator.

    Will often follow some kind of
    file_to_text -> clean_text -> text_to_token
    """

    _PROHIBITED_TAGS = ["start_parallel", "end_parallel"]

    def __init__(self):
        self.clear_pipeline()

    def add_stage(self, f, tag=None, stage_opts=None):
        if tag is not None and tag in self._funcs:
            raise KeyError("Tag already exists. Either chose another "
                           "tag or use replace_stage instead")
        return self._set_stage(f, tag=tag,
                               stage_opts=stage_opts)

    def replace_stage(self, f, tag=None, stage_opts=None):
        if tag is not None and tag not in self._funcs:
            raise KeyError("Tag does not exists. Either chose an existing "
                             "tag or use add_stage instead")
        return self._set_stage(f, tag=tag,
                               stage_opts=stage_opts)

    def _set_stage(self, f, tag=None, stage_opts=None):

        if stage_opts is None:
            stage_opts = dict()

        tag = self._process_tag(tag)
        self._funcs[tag] = partial(f, **stage_opts)

        return self

    def delete_stage(self, tag):
        if tag not in self._funcs:
            raise KeyError("Tag does not exists.")
        del self._func[tag]

    def _process_tag(self, tag):
        if isinstance(tag, str) and any(word in tag for word in self._PROHIBITED_TAGS):
            raise NameError(f"tag can't have {self._PROHIBITED_TAGS} on it")
        if tag is None:
            # Deals with the last inserted id and custom tags
            while self._curr_id in self._funcs:
                self._curr_id += 1
            tag = self._curr_id
        return tag

    def apply(self, x):
        func_iter = iter(self._funcs.values())
        for func in func_iter:
            if isinstance(func, StartParallel):
                stages = list()
                func = next(func_iter)
                while not isinstance(func, EndParallel):
                    stages.append(func)
                    func = next(func_iter)
                x = multi_process_stages(x, stages, func.workers, func.batch_size)
            else:
                x = func(x)
        return x

    def clear_pipeline(self):
        self._curr_id = 0
        self._parallel_sections = 0
        self._funcs = OrderedDict()

    def define_parallel_section(self, workers, batch_size, start, end=None):

        self._parallel_sections += 1
        suffix = '_'+str(self._parallel_sections)

        new_dict = OrderedDict()
        funcs_iter = iter(self._funcs.items())

        for tag, func in funcs_iter:
            if tag == start:
                new_dict["start_parallel"+suffix] = StartParallel()
                new_dict[tag] = func
                break
            new_dict[tag] = func
        else:
            raise KeyError(f"{start} not a stage tag")

        if end is None:
            new_dict["end_parallel"+suffix] = EndParallel(workers)

        for tag, func in funcs_iter:
            new_dict[tag] = func
            if tag == end:
                new_dict["end_parallel"+suffix] = EndParallel(workers, batch_size)
                break
            if isinstance(func, _ParallelIndicator):
                raise Exception("Parallel sections cannot intersect")
        else:
            raise KeyError(f"{end} not a stage tag")

        for tag, func in funcs_iter:
            new_dict[tag] = func

        self._funcs = new_dict


class EmbeddingPipeline(_Pipeline):

    def __init__(self, source_gen=None, seed_words=None,
                 tfidf_config=None):

        super().__init__()

        self.source_gen = source_gen
        self.seed_words = seed_words if seed_words is not None else dict()

        self._doc_names = OrderedDict()

        self._emb_weights = None

        if tfidf_config is None:
            tfidf_config = dict()

        self._tfidf = TfidfVectorizer(**tfidf_config)
        self._tfidf_trained = False
        self._tfidf_res = None

    @property
    def doc_names(self):
        return self._doc_names

    @doc_names.setter
    def doc_names(self, doc_names):
        self._doc_names = doc_names

    @property
    def tfidf(self):
        if self._tfidf is None:
            raise AttributeError("TFIDF model have not been set")
        return self._tfidf

    @tfidf.setter
    def tfidf(self, tfidf):
        self._tfidf = tfidf

    @property
    def tfidf_res(self):
        if self._tfidf_res is None:
            raise AttributeError("TFIDF results have not been set")
        return self._tfidf_res

    @tfidf_res.setter
    def tfidf_res(self, tfidf_res):
        self._tfidf_res = tfidf_res

    @property
    def emb_weights(self):
        if self._emb_weights is None:
            raise AttributeError("Embedding Weights have not been set")
        return self._emb_weights

    @emb_weights.setter
    def emb_weights(self, weights):
        if not isinstance(weights, np.ndarray):
            raise TypeError(f"weights must be of type {np.ndarray}")
        self._emb_weights = weights

    def extract_emb_weights(self, model):
        raise NotImplementedError()

    def id_to_words(self, tokens):
        raise NotImplementedError()

    def word_to_id(self, word):
        raise NotImplementedError()

    def id_to_words(self, tokens):
        raise NotImplementedError()

    def id_to_emb(self, wid):
        raise NotImplementedError()

    def word_to_emb(self, wid):
        return self.id_to_emb(self.word_to_id(wid))

    def cosine_similarity(self, word_emb):
        return ((self.emb_weights @ word_emb.T)
                / (vec_len(word_emb) * vec_len(self.emb_weights)))

    def get_closest_ids(self, word_emb, n=5):
        return np.argsort(self.cosine_similarity(word_emb))[-1:-n-1:-1]

    def get_word_dict(self, n=50):
        return {word: self.id_to_words(self.get_closest_ids(
                          np.mean(self.word_to_emb(seeds),
                                  axis=0),
                          n=n
                      ))
                for word, seeds in self.seed_words.items()}

    def gen_from_source(self):
        # Apply should take in one source item and return an iterator that
        # yields doc_name, doc_text tuples.

        # Making apply return iterators allows us to adapt to situations
        # where the same source input yields multiple documents (e.g. a
        # single file containing multiple documents or specifying root
        # directory instead of each text file.
        if self.source_gen is None:
            raise AttributeError("Must set source gen before generating "
                                 "from source")
        for processed in self.apply(self.source_gen):
            yield processed

    def process_source(self, dir_path=None, replace_source=True):

        if dir_path is None:
            dir_path = "processed_source"

        dir_path = Path(dir_path)
        if not dir_path.exists():
            dir_path.mkdir()

        added_files = []
        # If generator returns text from one document at a time, this
        # avoids opening and closing the same file.
        for doc_name, doc_text in self.gen_from_source():
            file_path = dir_path.joinpath(doc_name+".txt")
            added_files.append(str(file_path))
            with open(file_path, "w") as file_writer:
                file_writer.write(doc_text)

        # Replace pipeline with default retrieval
        if replace_source:
            self.source_gen = tuple(added_files)
            self.clear_pipeline()
            self.add_stage(file_to_text, tag="file_to_text")

    def _gen_and_name(self):
        # This is necessary as the CountVectorizer does not keep
        # document names and takes the document text only.
        for i, (doc_name, doc_text) in enumerate(self.gen_from_source()):
            self._doc_names[doc_name] = i
            yield doc_text

    def train_tfidf(self, reset=False, save=False):

        if self._tfidf_trained and not reset:
            raise Exception("Bag-of-words has already been trained, if you "
                            "would like to override it, set reset=True in "
                            "this method.")

        self._tfidf_res = self._tfidf.fit_transform(self._gen_and_name())

        self._tfidf_trained = True
        self._save_obj(save, self._tfidf, "tfidf.pkl")
        self._save_obj(save, self._tfidf_res, "tfidf_res.pkl")

    def train_weights(self, save=False):
        raise NotImplementedError()

    def save(self, name=None):
        if name is None:
            name = "embedding_dict_model.pkl"
        self._save_obj(True, self, name)

    def _save_obj(self, save, obj, default_name):
        if save:
            save = save if isinstance(save, (str, Path)) else default_name
            dump(obj, save)
