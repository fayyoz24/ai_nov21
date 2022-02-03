import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.metrics import accuracy_score as score

class IRIS:
    def preprocess(path):
        colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
        df = pd.read_csv(path, names=colnames)
        iris = load_iris()
        X = df.values[:, :4]
        y = iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        
        return X_train, X_test, y_train, y_test

    def poly():
        olma = IRIS.preprocess("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

        clf = svm.SVC(kernel='poly')
        clf.fit(olma[0], olma[2])
        y_pred = clf.predict(olma[1])
        return (f'Accuracy: {score(olma[3], y_pred)}')
        # print(plot_confusion_matrix(clf, olma[0], olma[3]))

    def rbf():
        olma = IRIS.preprocess("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

        clf_rbf = svm.SVC(kernel='rbf')
        clf_rbf.fit(olma[0], olma[2])
        y_pred_rbf = clf_rbf.predict(olma[1])
        return (f'Accuracy: {score(olma[3], y_pred_rbf)}')
        # print(plot_confusion_matrix(clf, olma[0], olma[3]))
    
    def sigm():
        olma = IRIS.preprocess("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

        clf_sigm = svm.SVC(kernel='sigmoid')
        clf_sigm.fit(olma[0], olma[2])
        y_pred_sigm = clf_sigm.predict(olma[1])
        return (f'Accuracy: {score(olma[3], y_pred_sigm)}')
        # print(plot_confusion_matrix(clf, olma[0], olma[3]))
  


print(IRIS.rbf())