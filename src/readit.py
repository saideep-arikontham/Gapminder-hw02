import pandas as pd

def read_data():
    '''Read data from gapminder.tsv'''
    df = pd.read_csv('data/gapminder.tsv', delimiter = '\t')
    print(df.isna().sum())
    return df
