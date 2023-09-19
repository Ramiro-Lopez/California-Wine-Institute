import pandas as pd
from sklearn.model_selection import train_test_split


    
def wrangle_wine():
    '''
    acquire_wine will take the wine.csv files stored in the same folder and store them as appropiately named dataframes
    '''
    red_wine = pd.read_csv('winequality-red.csv')
    white_wine = pd.read_csv('winequality-white.csv')
    red_wine['wine_color'] = 'red'
    white_wine['wine_color'] = 'white'
    wine = pd.concat([white_wine, red_wine], ignore_index=False, axis=0)
    wine['wine_color'] = wine['wine_color'].map({'white': 0, 'red': 1})
    wine = wine.rename(columns = {'fixed acidity':'fixed_acidity', 'volatile acidity': 'volatile_acidity', 
                       'citric acid': 'citric_acid', 'residual sugar': 'residual_sugar',
                      'free sulfur dioxide': 'free_sulfur_dioxide', 'total sulfur dioxide': 'total_sulfur_dioxide'})
    wine = wine.drop(wine[wine['free_sulfur_dioxide'] == 289.0].index)
    wine = wine.drop(wine[wine['residual_sugar'] == 65.8].index)
    return wine


def split_data(df: pd.DataFrame) -> pd.DataFrame:
    '''splits data into train test and validate dataframes'''
    train, test = train_test_split(df, test_size=.2, random_state=117, stratify=df.quality)
    train, validate = train_test_split(train,
                                       test_size=.3,
                                       random_state=117, stratify=train.quality)
    return train, validate, test