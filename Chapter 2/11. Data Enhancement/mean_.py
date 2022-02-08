import numpy    as np

import pandas   as pd

from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from eda import eda

data = eda()

np.random.seed(0)

data['year'] = data['timestamp'].apply(lambda row: row[:4])
data['month'] = data['timestamp'].apply(lambda row: row.split('-')[2][:2] )
data['hour'] = data['timestamp'].apply(lambda row: row.split(':')[0][-2:] )

data.drop('timestamp', axis=1, inplace=True)

def data_enhancement(data):
    
    gen_data = data
    
    for season in data['season'].unique():
        seasonal_data = gen_data[gen_data['season'] == season]
        hum_std = seasonal_data['hum'].mean()
        wind_speed_std = seasonal_data['wind_speed'].mean()
        t1_std = seasonal_data['t1'].mean()
        t2_std = seasonal_data['t2'].mean()
        
        for i in gen_data[gen_data['season'] == season].index:
            if np.random.randint(2) == 1:
                gen_data['hum'].values[i] += hum_std/10
            else:
                gen_data['hum'].values[i] -= hum_std/10
                
            if np.random.randint(2) == 1:
                gen_data['wind_speed'].values[i] += wind_speed_std/10
            else:
                gen_data['wind_speed'].values[i] -= wind_speed_std/10
                
            if np.random.randint(2) == 1:
                gen_data['t1'].values[i] += t1_std/10
            else:
                gen_data['t1'].values[i] -= t1_std/10
                
            if np.random.randint(2) == 1:
                gen_data['t2'].values[i] += t2_std/10
            else:
                gen_data['t2'].values[i] -= t2_std/10

    return gen_data
def mean():
    y = data['cnt']
    x = data.drop(['cnt'], axis=1)


    cat_vars = ['season','is_weekend','is_holiday','year','month','weather_code']
    num_vars = ['t1','t2','hum','wind_speed']


    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y,
                                        test_size=0.2,
                                        random_state=0) # Recommended for reproducibility
                                    
    gen = data_enhancement(data)
    extra_sample = gen.sample(gen.shape[0] // 3)
    x_train = pd.concat([x_train, extra_sample.drop(['cnt'], axis=1 ) ])
    y_train = pd.concat([y_train, extra_sample['cnt'] ])


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
# tree_classifiers = {
#   "Decision Tree": DecisionTreeRegressor(),
#   "Extra Trees":   ExtraTreesRegressor(n_estimators=100),
#   "Random Forest": RandomForestRegressor(n_estimators=100),
#   "AdaBoost":      AdaBoostRegressor(n_estimators=100),
#   "Skl GBM":       GradientBoostingRegressor(n_estimators=100),
#   "XGBoost":       XGBRegressor(n_estimators=100),
#   "LightGBM":      LGBMRegressor(n_estimators=100),
#   "CatBoost":      CatBoostRegressor(n_estimators=100),
# }
# # ### END SOLUTIONv
# rang = abs(y_train.max()) + abs(y_train.min())
# tree_classifiers = {name: pipeline.make_pipeline(tree_prepro, model) for name, model in tree_classifiers.items()}

# results = pd.DataFrame({'Model': [], 'MSE': [], 'MAB': [], " % error": [], 'Time': []})

# for model_name, model in tree_classifiers.items():
    
#     start_time = time.time()
#     model.fit(x_train, y_train)
#     total_time = time.time() - start_time
        
#     pred = model.predict(x_test)
    
#     results = results.append({"Model":    model_name,
#                               "MSE": metrics.mean_squared_error(y_test, pred),
#                               "MAB": metrics.mean_absolute_error(y_test, pred),
#                               " % error": metrics.mean_squared_error(y_test, pred) / rang,
#                               "Time":     total_time},
#                               ignore_index=True)

