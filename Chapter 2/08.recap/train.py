from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
import data_handler as dh

def train_model():
    
    x_train, x_test, y_train, y_test, c_transformer, scaler  = dh.get_data(".\Chapter 2\08.recap\insurance.csv")
    
    xgb_r = XGBRegressor()
    gboosting_r = GradientBoostingRegressor(learning_rate=0.01, n_estimators=50)
    dtree_r = DecisionTreeRegressor(random_state=42, max_depth=4 )
    
    a = xgb_r.fit(x_train,y_train)
    b = gboosting_r.fit(x_train, y_train)
    c = dtree_r.fit(x_train, y_train)
    
    return a, b, c

print(train_model())



    
    
    


