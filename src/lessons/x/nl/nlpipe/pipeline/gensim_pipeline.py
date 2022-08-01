import re
import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.models import Word2Vec as wv 
from nlpipe.pipeline.embedding_pipeline import EmbeddingPipeline


class Word2VecPipeline(EmbeddingPipeline):

    def __init__(self, source_gen=None, seed_words=None,
                 tfidf_config=None,
                 model_config=None):

        super().__init__(source_gen=source_gen, seed_words=seed_words,
                         tfidf_config=tfidf_config)

        if model_config is None:
            model_config = dict()

        self.model_config = model_config
        self._model = None
        self._weight_update = False

    @property
    def model(self):
        if self._model is None:
            raise AttributeError("Model has not been fit")
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        self._weight_update = True

    @property
    def emb_weights(self):
        if self._weight_update:
            self.extract_emb_weights(self.model)
            self._weight_update = False
        return super().emb_weights

    def extract_emb_weights(self, model):
        self._emb_weights = model.wv.get_normed_vectors()
    

    def id_to_words(self, tokens):
        if isinstance(tokens, (list, tuple, np.ndarray)):
            return [self.id_to_words(tok) for tok in tokens]
        return self.model.wv.index_to_key[tokens]

    def word_to_id(self, words):
        if isinstance(words, (list, tuple, np.ndarray)):
            return [self.word_to_id(tok) for tok in words]
        return self.model.wv.key_to_index(words)

    def id_to_emb(self, id):
        return self.word_to_emb(self.id_to_words(id))

    def word_to_emb(self, key):
        return self.model.wv.get_vector(key)

    def get_word_dict(self, n=50):
        filtered_seeds = {word: [key for key in seeds
                                 if key in self.model.wv.key_to_index]
                          for word, seeds in self.seed_words.items()}
        filtered_seeds = {word: seeds for word, seeds in filtered_seeds.items()
                          if seeds != []}
        return {word: self.id_to_words(self.get_closest_ids(
                          np.mean(np.array([self.word_to_emb(key)
                                            for key in seeds]),
                                  axis=0),
                          n=50
                      ))
                for word, seeds in filtered_seeds.items()}

    def _gen_sentences(self):
        class _SentGenerator:
            def __init__(self, pipeline):
                self.pipeline = pipeline
            def __iter__(self):
                for doc_text in self.pipeline._gen_and_name():
                    for sent in sent_tokenize(doc_text):
                        # remove punctuation
                        sent = re.sub(r"[\.\?\!\;]", '', sent)
                        yield word_tokenize(sent)
        return _SentGenerator(self)

    def train_weights(self, save=False):
        self._model = Word2Vec(sentences=self._gen_sentences(),
                               **self.model_config)
        self._weight_update = True
        self._save_obj(save, self._model, "w2vec_model.pkl")
