import numpy as np
import pandas as pd

dataset = pd.read_csv("/home/andy/data/Restaurant_Reviews.tsv", delimiter="\t")
# library to clean data
import re

# Natural Language Tool Kit
import nltk

nltk.download("stopwords")

# to remove stopword
from nltk.corpus import stopwords

# for Stemming propose
from nltk.stem.porter import PorterStemmer

# Initialize empty array
# to append clean text
corpus = []

# 1000 (reviews) rows to clean
for i in range(0, 1000):
    # column : "Review", row ith
    review = re.sub("[^a-zA-Z]", " ", dataset["Review"][i])

    # convert all cases to lower cases
    review = review.lower()

    # split to array(default delimiter is " ")
    review = review.split()

    # creating PorterStemmer object to
    # take main stem of each word
    ps = PorterStemmer()

    # loop for stemming each word
    # in string array at ith row
    review = [
        ps.stem(word) for word in review if not word in set(stopwords.words("english"))
    ]

    # rejoin all string array elements
    # to create back into a string
    review = " ".join(review)

    # append each string to create
    # array of clean text
    corpus.append(review)

print(corpus)
