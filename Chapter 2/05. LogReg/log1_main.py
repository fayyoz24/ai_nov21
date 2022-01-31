from sklearn.datasets import load_breast_cancer
from log1 import LogisticRegression


#Loading the data
data = load_breast_cancer()
 
#Preparing the data
x = data.data
y = data.target
 
#creating the class Object
regressor = LogisticRegression(x,y)
 
#
regressor.fit(0.1 , 50000)
 
 
y_pred = regressor.predict(x,0.5)
 
print('accuracy -> {}'.format(sum(y_pred == y) / y.shape[0]))