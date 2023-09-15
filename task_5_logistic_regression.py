# -*- coding: utf-8 -*-
"""Task 5 logistic_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sbOtunesftA2YyafXE3H6rdLGLPPWF6S

# Logistic Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('creditcard.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(y)

"""# Data Handling"""

#from sklearn.impute import SimpleImputer
#imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
#imputer.fit(X[:, 1:3])
#X[:, 1:3] = imputer.transform(X[:, 1:3])

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""## Training the Logistic Regression model on the Training set"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

"""## Predicting the Test set results"""

y_pred = classifier.predict(X_test)
#print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)