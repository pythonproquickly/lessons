# nltk way
#
import nltk
from nltk.util import ngrams
text = "Hi How are you? i am fine and you"
token = nltk.word_tokenize(text)
trigrams = ngrams(token, 3)
print(list(trigrams))


# my way
def trigrams(tokens):
    return zip(tokens, tokens[1:], tokens[2:])


tokens = "this sentence want check lots words need sentence want check lots".split(' ')
tg = trigrams(tokens)
print(list(tg))


from collections import Counter
mc = Counter(trigrams(tokens)).most_common(3)
print(mc)
