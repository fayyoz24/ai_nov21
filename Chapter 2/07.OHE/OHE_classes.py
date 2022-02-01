
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
        
    def dec_trees():
        df = Tree_algorithms.preprocess()
        y = df['smoker']
        X = df.drop(['smoker'], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        dctr = DecisionTreeRegressor(random_state=0)
        dctr.fit(X_train, y_train)

        train = dctr.score(X_train, y_train)
        test = dctr.score(X_test, y_test)
        return (f'training accuracy:{train}\n testing accuracy: {test}')
    
    def rand_forest():
        df = Tree_algorithms.preprocess()
        y = df['smoker']
        X = df.drop(['smoker'], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        randf = RandomForestRegressor(random_state=0)
        randf.fit(X_train, y_train)

        train = randf.score(X_train, y_train)
        test = randf.score(X_test, y_test)
        return (f'training accuracy:{train}\n testing accuracy: {test}')
        
    def ext_rand_tress():
        df = Tree_algorithms.preprocess()
        y = df['smoker']
        X = df.drop(['smoker'], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        ex_rand_tr = ExtraTreesRegressor(random_state=0)
        ex_rand_tr.fit(X_train, y_train)

        train = ex_rand_tr.score(X_train, y_train)
        test = ex_rand_tr.score(X_test, y_test)
        return (f'training accuracy:{train}\n testing accuracy: {test}')
        
    def adaboosting():
        df = Tree_algorithms.preprocess()
        y = df['smoker']
        X = df.drop(['smoker'], axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        adab = AdaBoostRegressor(random_state=0)
        adab.fit(X_train, y_train)

        train = adab.score(X_train, y_train)
        test = adab.score(X_test, y_test)
        return (f'training accuracy:{train}\n testing accuracy: {test}')
        

print(Tree_algorithms.ext_rand_tress())