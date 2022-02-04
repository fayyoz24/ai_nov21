import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def preprocess(path):

    df = pd.read_csv(path)

    X, y = df.values[:, :-1], df.values[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=0)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler