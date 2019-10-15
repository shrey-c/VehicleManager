import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re
import pickle
from sklearn.externals import joblib
#print (1000)
#classifier = joblib.load('model.pkl')
#print(1)
#predict = classifier.predict(msg_test)
#print (2)
#print (predict)
from trained_model2 import classified
a = classified("my name ios apple")
print(a)
print("hi this is me")