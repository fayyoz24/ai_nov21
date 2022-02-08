import numpy    as np
from numpy.testing._private.utils import decorate_methods
import pandas   as pd
import seaborn  as sb
import matplotlib.pyplot as plt
import sklearn  as skl
import time

from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn import set_config
from eda import eda


data = eda()

np.random.seed(0)

data['year'] = data['timestamp'].apply(lambda row: row[:4])
data['month'] = data['timestamp'].apply(lambda row: row.split('-')[2][:2] )
data['hour'] = data['timestamp'].apply(lambda row: row.split(':')[0][-2:] )

data.drop('timestamp', axis=1, inplace=True)


def data_enhancement():

    data = eda()
    data['t1_t2'] = data.apply(lambda row: (row['t1']+row['t2'])/2, axis=1)
    # data['hum_win'] = data.apply(lambda row: row['hum']*row['wind_speed'])
    data = data.drop(['t1'], axis=1)
    data = data.drop(['t2'], axis=1)
    
    gen_data = data
    
    return gen_data

def new_col():

    data = data_enhancement()
   
    y = data['cnt']
    x = data.drop(['cnt'], axis=1)

    cat_vars = ['season','is_weekend','is_holiday','year','month','weather_code']
    num_vars = ['t1_t2','hum','wind_speed'] # multicollinearity problem

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                        test_size=0.2,
                                        random_state=0  # Recommended for reproducibility
                                    )

    transformer = preprocessing.PowerTransformer()
    y_train = transformer.fit_transform(y_train.values.reshape(-1,1))
    y_test = transformer.transform(y_test.values.reshape(-1,1))

    num_4_treeModels = pipeline.Pipeline(steps=[
        ('imputer', impute.SimpleImputer(strategy='constant', fill_value=-9999)),
    ])

    cat_4_treeModels = pipeline.Pipeline(steps=[
        ('imputer', impute.SimpleImputer(strategy='constant', fill_value='missing')),
        ('ordinal', preprocessing.OrdinalEncoder()) # handle_unknown='ignore' ONLY IN VERSION 0.24
    ])

    tree_prepro = compose.ColumnTransformer(transformers=[
        ('num', num_4_treeModels, num_vars),
        ('cat', cat_4_treeModels, cat_vars),
    ], remainder='drop') # Drop other vars not specified in num_vars or cat_vars

    return x_train, x_test, y_train, y_test, tree_prepro