from sentiment.dataset.slang_df import generate_slang
import pandas as pd
import numpy as np

#dealing with corpus
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#indonesian word stemmer and stopword removal
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

##create function used to change texts to lowercase
def caseFolding(text):
    processed = text.lower()
    return processed

##create function used to remove punctuations
def removePunctuation(text):
    processed = "".join(x for x in text if x not in ("?", ",", ".", ";", "@", ":", "!", "'", "-"))
    return processed

##create function to delete numbers
def removeNumbers(text):
    processed = re.sub(r"\d+", "", text)
    return processed

def tokenizing(text):
    processed = text.split()
    return processed

##create function to delete stopwords
def IDStopwordRemoval(text):
    stopwordFactory = StopWordRemoverFactory()
    stopword = stopwordFactory.get_stop_words()

    stopwords_exclude = ['tidak', 'nggak', 'tetapi', 'tapi']
    for i in stopwords_exclude:
        stopword.remove(i)

    dictionary = ArrayDictionary(stopword)
    stopwords = StopWordRemover(dictionary)

    processed = stopwords.remove(text)

    return processed

##create function to stem words
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def indonesianStemmer(text):
    # creating stemmer
    processed = stemmer.stem(text)
    return processed

normalized_dict = {}
slang_df = generate_slang()

for index, row in slang_df.iterrows():
    if row[0] not in normalized_dict:
        normalized_dict[row[0]] = row[1]
        
def normalize_review(text):
  # tokenize
  list_text = word_tokenize(text)
  # ubah bahasa alay
  list_text = [normalized_dict[term] if term in normalized_dict else term for term in list_text]
  # gabung kembali kalimat
  text = " ".join(list_text)
  return text


def preprocessing(text):
    processed = ""
    processed = caseFolding(text)
    processed = removePunctuation(processed)
    processed = removeNumbers(processed)
    processed = IDStopwordRemoval(processed)
    processed = indonesianStemmer(processed)
    processed = normalize_review(processed)
    return processed