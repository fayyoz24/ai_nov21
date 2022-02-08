import pandas as pd
def eda():
    data = pd.read_csv('./london_merged.csv')
    data['year'] = data['timestamp'].apply(lambda row: row[:4])
    data['month'] = data['timestamp'].apply(lambda row: row.split('-')[2][:2] )
    data['hour'] = data['timestamp'].apply(lambda row: row.split(':')[0][-2:] )

    # data.drop('timestamp', axis=1, inplace=True)

    data['cnt'].describe()
    data.corr().style.background_gradient(cmap='RdPu')

    #correlations between our target and other features
    corr_target = round(data.corr().iloc[0].sort_values(ascending=False), 3)
    print(corr_target)

    return data
