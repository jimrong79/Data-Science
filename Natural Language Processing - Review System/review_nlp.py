# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:00:30 2020

@author: jimro
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("Restaurant_Reviews.tsv", sep = '\t', quoting = 3)

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []


for i in range(dataset.shape[0]):
  # remove special character like "" , which are not a-z and A-Z
  review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
  
  # only lowercase
  review = review.lower()

  # split review to different words
  review = review.split()

  # apply stemming to all the words and also leave the stop words out
  ps = PorterStemmer()
  all_stopwords = set(stopwords.words('english'))
  all_stopwords.remove("not")
  review = [ps.stem(word) for word in review if not (word in (all_stopwords))] 

  review = " ".join(review)
  corpus.append(review)

# Creating the Bag of Words model; Tokenization
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


# optimize max_feature number. Turns out around 150 gave the best performance of accuracy around 0.75
# max_acc = 0
# max_acc_feature = 0

# for i in range(20, 1000, 1):
#   cv = CountVectorizer(max_features = i)
#   X = cv.fit_transform(corpus).toarray()
#   y = dataset.iloc[:, -1].values
#   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#   classifier = GaussianNB()
#   classifier.fit(X_train, y_train)
#   y_pred = classifier.predict(X_test)
#   acc = accuracy_score(y_test, y_pred)
#   if acc >= max_acc:
#     print ("max_feature: {} has max acc so far: {}".format(i, acc))
#     max_acc = acc

