
from posixpath import split
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder


class Tree_algorithms:

    def preprocess():
        ord = OrdinalEncoder()
        data = 'insurance.csv'
        df = pd.read_csv(data)
        df[['sex', 'smoker', 'region']] = ord.fit_transform(df[['sex', 'smoker', 'region']])

        return df

    def split():
        df = Tree_algorithms.preprocess()
        X, y = df.iloc[:, :6], df.iloc[:, 6]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        return list(X_train, X_test, y_train, y_test)


    def dec_trees():
        split = Tree_algorithms.split()
        dctr = DecisionTreeRegressor(random_state=0)
        dctr.fit(split[0], split[2])

        train = dctr.score(split[0], split[2])
        test = dctr.score(split[1], split[3])
        return (f'training accuracy:{train}\n testing accuracy: {test}')
    
    def rand_forest():
        split = Tree_algorithms.split()
        randf = RandomForestRegressor(random_state=0)
        randf.fit(X_train, y_train)

        train = randf.score(split[0], split[2])
        test = randf.score(split[1], split[3])
        return (f'training accuracy:{train}\n testing accuracy: {test}')
        
    def ext_rand_tress():
        df = Tree_algorithms.preprocess()
        y = df['smoker']
        X = df.drop(['smoker'], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        ex_rand_tr = ExtraTreesRegressor(random_state=0)
        ex_rand_tr.fit(X_train, y_train)

        train = ex_rand_tr.score(split[0], split[2]
        test = ex_rand_tr.score(split[1], split[3])
        return (f'training accuracy:{train}\n testing accuracy: {test}')
        
    def adaboosting():
        df = Tree_algorithms.preprocess()
        y = df['smoker']
        X = df.drop(['smoker'], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        adab = AdaBoostRegressor(random_state=0)
        adab.fit(X_train, y_train)

        train = adab.score(split[0], split[2]
        test = adab.score(split[1], split[3])
        return (f'training accuracy:{train}\n testing accuracy: {test}')
        

print(Tree_algorithms.ext_rand_tress())