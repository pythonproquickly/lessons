import numpy as np
import pandas as pd

from nlpipe.pipeline.embedding_pipeline import EmbeddingPipeline


class HuggingFacePipeline(EmbeddingPipeline):

    def __init__(self, source_gen=None, seed_words=None,
                 tfidf_config=None,
                 model=None):

        super().__init__(source_gen=source_gen, seed_words=seed_words,
                         tfidf_config=tfidf_config)

        self._tokenizer = None

        if model is not None:
            self.extract_emb_weights(model)

    @property
    def tokenizer(self):
        if self._tokenizer is None:
            raise AttributeError("Tokenizer is not set")
        return self._tokenizer

    @tokenizer.setter
    def tokenizer(self, tokenizer):
        self._tokenizer = tokenizer

    # def get_overall_closest_ids(self, word_emb, n=5):
    #     return pd.unique(np.argsort(self.cosine_similarity(word_emb).T, axis=None)
    #                      % self.emb_weights.shape[0])[-1:-n-1:-1]

    # def get_word_dict(self, n=50):
    #     return {word: self.id_to_words(self.get_overall_closest_ids(
    #                       self.word_to_emb(seeds), n=50
    #                   ))
    #             for word, seeds in self.seed_words.items()}

    def extract_emb_weights(self, model):
        self._emb_weights = (model.bert.embeddings.word_embeddings
                             .weight.detach().clone().numpy())

    def id_to_words(self, tokens):
        return self.tokenizer.batch_decode(np.atleast_2d(tokens).T)

    def word_to_id(self, word):
        return self.tokenizer(word, return_tensors="np", padding=True)["input_ids"][:, 1]

    def id_to_emb(self, wid):
        return self.emb_weights[wid]

    def train_weights(self):
        raise NotImplementedError("Weight training not implemented for "
                                  "Huggingface pretrained models")
