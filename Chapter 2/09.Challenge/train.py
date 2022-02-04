from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier

import data_handler as dh

import pandas as pd
import numpy as np

import warnings

from sklearn.model_selection import cross_val_score, learning_curve
from sklearn.metrics import accuracy_score as score, plot_confusion_matrix as plt_m
from sklearn.model_selection import KFold


class Models:

    def svc():
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')
        model = SVC(kernel='rbf')
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = score(y_test, preds)

        return f'Accuracy from SVM.SVC:      {acc *100} %'

    def lr():
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')

        model = LogisticRegression()
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = score(y_test, preds)

        return f'Accuracy from LogisticRegression:       {acc *100} %'
        
    def rfc():
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')

        model = RandomForestClassifier(n_estimators=100, max_depth=4)
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = score(y_test, preds)

        return f'Accuracy from RandomForestClassifier:        {acc *100} %'

    def knc():
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')

        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = score(y_test, preds)

        return f'Accuracy from KNeighborsClassifier:       {acc *100} %'        

    def gbc():
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')

        model = GradientBoostingClassifier(n_estimators=500, learning_rate=0.1, max_depth=1, random_state=0)
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = score(y_test, preds)

        return f'Accuracy from GradientBoostingClassifier:      {acc *100} %'

    def xgbc():
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')

        model = XGBClassifier()
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = score(y_test, preds)
        warnings.filterwarnings("ignore")

        return f'Accuracy from XGBClassifier:       {acc *100} %'
        
    def dtc():
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = dh.preprocess('./heart.csv')

        model = DecisionTreeClassifier()
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        acc = score(y_test, preds)
        warnings.filterwarnings("ignore")

        return f'Accuracy from: DecisionTreeClassifier:        {acc *100} %'

print(Models.svc())