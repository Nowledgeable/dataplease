from data_generator import *

def generate_transaction(file_name, nrows):

    payment_types = ['card', 'transfer', 'cheque']

    names = [
        'Carrefour',
        'Renault',
        'Nissan',
        'Tesla',
        'Valeo',
        'Monoprix',
        'CapGemini',
        'Chevron',
        'ConocoPhillips',
        'Exxon Mobil',
        'McKesson',
        'General Motos',
        'Activision Blizard'
    ]

    countries = [
        'FR',
        'SWI',
        'ITA',
        'SPA',
        'US',
        'GER',
        'SP',
        'JAP',
        'UK',
        'CHI',
    ]

    requirements = [
        {
            'name': 'agency_id',
            'generator': lambda nrows, df: np.random.randint(1, 10000, nrows)
        },

        {
            'name': 'account_sender_name',
            'generator': lambda nrows, df: np.random.choice(names, nrows)
        },

        {
            'name': 'country_sender',
            'generator': lambda nrows, df: np.random.choice(countries, nrows)
        },

        {
            'name': 'account_receiver_name',
            'generator': lambda nrows, df: np.random.choice(names, nrows)
        },

        {
            'name': 'country_receiver',
            'generator': lambda nrows, df: np.random.choice(countries, nrows)
        },
        {
            'name': 'amount',
            'generator': lambda nrows, df: np.random.randint(1, 10000000, nrows)
        },
        {
            'name': 'payment_type',
            'generator': lambda nrows, df: np.random.choice(payment_types, nrows)
        },
        {
            'name': 'datetime_timestamp',
            'generator': lambda nrows, df: 1000 * np.arange(nrows)
        },

    ]

    df = generate_df(requirements, nrows)
    df.to_csv(file_name, index=False)



generate_transaction('transactions_big.csv', 1000)