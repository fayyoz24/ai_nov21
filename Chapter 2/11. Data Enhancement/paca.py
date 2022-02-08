from eda import eda
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler as scaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import PowerTransformer
def pca_():
    data = eda()

    y = data['cnt']
    x = data.drop(['cnt'], axis=1)

    pca = PCA(n_components=3)
    x_red_dim = pca.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_red_dim, y,
                                        test_size=0.2,
                                        random_state=0)  

    x_train_scaled=scaler.fit_transform(x_train)
    x_test_scaled=scaler.transform(x_test)
    transformer = PowerTransformer()
    y_train = transformer.fit_transform(y_train.values.reshape(-1,1))
    y_test = transformer.transform(y_test.values.reshape(-1,1))

    return x_train_scaled, x_test_scaled, y_train, y_test