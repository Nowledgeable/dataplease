from data_generator import *

import numpy as np

def generate_price(df, nrows):

    price = 45000 * np.log(1 + df['size'])
    price += 20000 * (df['nb_rooms'] - 1)

    price += 20000 * (df['orientation'] == 'Sud').astype('int')
    price -= 20000 * (df['orientation'] == 'Nord').astype('int')
    price += 1000 * (df['orientation'] == 'Ouest').astype('int')
    price -= 3000 * (df['orientation'] == 'Est').astype('int')

    price += 50000 * (df['garden'] == 1).astype('int')

    return price

def houses(name):

    requirements = [

        {
            'name': 'size',
            'generator': lambda nrows, df: np.abs(150 + 50 * np.random.randn(nrows))
        },
        {
            'name': 'nb_rooms',
            'generator': lambda nrows, df: np.random.randint(1, 4, nrows)
        },
        {
            'name': 'garden',
            'generator': lambda nrows, df: np.random.randint(0, 2, nrows)
        },
        {
            'name': 'orientation',
            'generator': lambda nrows, df: np.random.choice(['Sud', 'Est', 'Ouest', 'Nord'], nrows)
        },
        {
            'name': 'price',
            'generator': lambda nrows, df: generate_price(df, nrows)
        },
    ]

    df = generate_df(requirements, 40)

    #print(df.describe())
    #print(df.head())

    df.to_csv(name, index=False)
    #df_to_sql_file('houses', df, 'houses.sql')

    #df_with_duplicates = df.append([df[:10], df[30:50], df[100:120]])

    #df_to_sql_file('houses', df_with_duplicates, 'houses_with_duplicate.sql')


def house_size_is_sold_in_six_month():
    requirements = [
        {
            'name': 'size',
            'generator': lambda nrows, df: 150 + 50 * np.random.randn(nrows),
        },
        {
            'name': 'sold_in_six_month',
            'is_target': True,
            'generator': lambda nrows, df: df['size'] > 150
        }
    ]

    df = generate_df(requirements, nrows=800000)

    df.to_csv('house_classification.csv')

houses('houses.csv')
