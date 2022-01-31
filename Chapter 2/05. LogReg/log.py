from sklearn.datasets import load_breast_cancer 
import pandas as pd
import numpy as np


dataset = load_breast_cancer()
df_breast = pd.DataFrame(dataset.data, columns=dataset.feature_names)
print(df_breast.head())
length = len(df_breast)
print(length)
df_breast['target'] = dataset.target
df = df_breast[:(2*length//3)]
df_test = df_breast[(2*length//3):]
print(df.head)
df_1 = df[df['target'] == 1]
df_0 = df[df['target'] == 0]
df_0 = df_0.drop('target', axis=1)
df_1 = df_1.drop('target', axis=1)

df0 = df_0.values
df1 = df_1.values

sum_dot0 = 0
for i in range(df0.shape[0]):
    ar_1 = np.ones(df0.shape[1])
    ar_1.reshape(df0.shape[1],1)
    dot = np.dot(ar_1, df0[i])
    sum_dot0 += dot
mean_0 = sum_dot0 / df0.shape[0]

sum_dot1 = 0
for i in range(df1.shape[0]):
    ar_1 = np.ones(df0.shape[1])
    ar_1.reshape(df0.shape[1],1)
    dot = np.dot(ar_1, df1[i])
    sum_dot1 += dot
mean_1 = sum_dot1 / df1.shape[0]

df_test1 = df_test.drop('target', axis=1)
df_test_ar = df_test1.values

sum_dot = []
for i in range(df_test_ar.shape[0]):
    ar_1 = np.ones(df0.shape[1])
    ar_1.reshape(df0.shape[1],1)
    dot = np.dot(ar_1, df_test_ar[i])
    delta_0 = np.abs(dot-mean_0)
    delta_1 = np.abs(dot-mean_1)
    if delta_0 < delta_1:
        sum_dot.append(0)
    else:
        sum_dot.append(1)

a = 0
for i in range(len(df_test['target'].values)):
    if df_test['target'].values[i] == sum_dot[i]:
        a+=1
b = len(df_test['target'].values)

print(f'accuracy: {a/b}')
print(sum_dot)
print(df_test['target'].values)