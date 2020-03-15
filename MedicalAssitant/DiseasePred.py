#import all packages and modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.externals import joblib
#importing nltk 
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#import re
#for bag_of_words model
from sklearn.feature_extraction.text import CountVectorizer

#loading dataset
train = pd.read_csv("Training.csv")
test = pd.read_csv("Testing.csv")

y_train = train['prognosis'].values
Y_train = np.ravel(y_train)

X_train = train.columns.values
X_train = np.delete(X_train,-1)

l2=[]
for x in range(0,len(X)):
    l2.append(0)

le = LabelEncoder()
X1 = le.fit_transform(X)
Y1 = le.fit_transform(y)
X1 = X.reshape(1,-1)
Y1 = Y.reshape(1,-1)

rfc = RandomForestClassifier()
rfc = rfc.fit(X1,Y1)

# calculating accuracy-------------------------------------------------------------------
y_pred = rfc.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(accuracy_score(y_test, y_pred,normalize=False))
psymptoms = ['loss_of_balance','visual_disturbances','depression','chest_pain']

for k in range(0,len(X)):
    for z in psymptoms:
        if(z==X[k]):
            l2[k]=1
inputtest = [l2]
predict = rfc.predict(inputtest)
predicted=predict[0]

h='no'
for a in range(0,len(Y)):
    if(predicted == a):
        h='yes'
        break

    if (h=='yes'):
        # t2.delete("1.0", END)
        # t2.insert(END, X[a])
        print(y[a])
    else:
        # t2.delete("1.0", END)
        # t2.insert(END, "Not Found")
        print("Not Found")

