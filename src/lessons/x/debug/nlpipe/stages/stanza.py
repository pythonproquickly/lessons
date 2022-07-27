import re

import stanza


def stanza_text_processor(gen, *args, **kwargs):
    nlp = stanza.Pipeline(*args, **kwargs, verbose=False)
    for text in gen:
        if isinstance(text, tuple):
            yield text[0], nlp(text[1])
        else:
            yield nlp(text)


def process_annotated_text(gen):
    for doc in gen:

        has_name = isinstance(doc, tuple)

        if has_name:
            name, doc = doc

        ret = []
        last_ner = ''

        for sent in doc.sentences:
            for token in sent.tokens:
                this_ner = token.ner.split('-')[-1]
                if this_ner not in ["O", last_ner]:
                    ret.append(this_ner)
                    break
                for word in token.words:
                    ret.append(word.lemma)
                last_ner = this_ner

        if has_name:
            ret = name, ret

        yield ret
