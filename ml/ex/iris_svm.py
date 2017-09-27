#!/usr/bin/env python3

from sklearn import svm
from sklearn import datasets
import pickle

# Get a Support Vector Classifier
clf = svm.SVC()

# Get some data
iris = datasets.load_iris()

# Separate the data and the target (labels)
X, y = iris.data, iris.target

# Do the actual learning
clf.fit(X, y)

# Predict something using the loaded model
print("Prediction:", clf.predict(X[0:1]))
print("Label:", y[0])

      
