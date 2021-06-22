#nltk.download('punkt')
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence=[stem(w) for w in tokenized_sentence]
    bag=np.zeros(len(all_words),dtype=np.float)
    for idx,w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag

# sentence = ["hello","how","are","you"]
# words=["hi","hello","I","you","bye","thank","cool"]
# bag=bag_of_words(sentence,words)
# print(bag)

# a="Hello how are you? Bro"
# print(a)
# a=tokenize(a)
# print(a)

# words = ["Organize","organizes","organizing"]
# stemmed_words=[stem(w) for w in words]
# print(stemmed_words)