
import random

payment_types = [ 'cheque','card', 'transfer']

receivers = {
    '1': [
        {
            "account_receiver_name": "Carrefour",
            "country_receiver": 'FR',
            'agency_id': 1
        },
        {
            "account_receiver_name": "Monoprix",
            "country_receiver": 'FR',
            'agency_id': 1
        },
    ],
    '2':[
        
        {
            "account_receiver_name": "Renault",
            "country_receiver": 'FR',
            'agency_id': 2
        },
        {
            "account_receiver_name": "Valeo",
            "country_receiver": 'FR',
            'agency_id': 2
        },
    ],
    '3': [
         {
            "account_receiver_name": "CapGemini",
            "country_receiver": 'FR',
            'agency_id': 3
        },
        {
            "account_receiver_name": "Thales",
            "country_receiver": 'FR',
            'agency_id': 3
        },
    ]
}
   
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

names = [
    {
        "name": 'Nissan',
        "country": "JAP"
    },
    {
        "name": "Tesla",
        "country": "US"
    },
    {
        "name": "EDF",
        "country": "FR"
    },
    {
        
        "name":'XXXX',#anonymized consumer
        "country": lambda :random.choice(countries)
    }
]


def get_sender():

    sender = random.choice(names)
    if callable(sender["country"]):
        sender["country"] = sender['country']()
    return {
        'account_sender_name' : sender['name'],
        'country_sender': sender['country']
    }

def get_payment_type(sender):

    if 'XX' in sender['account_sender_name']:
        return random.choice(payment_types[:-1])

    return payment_types[-1]

def generate_receiver_transaction(agency_id: str):
    """
        generate a transaction for which the receiver is a customer of an agency (id = 1 to 3)
        the sender may not be a customer of the bank
    """
    agency_id = str(agency_id)
    receiver = random.choice(receivers[agency_id])
    sender = get_sender()

    return { **receiver, **sender, **{
        "amount": random.randint(1000, 1000000),
        'payment_type' : get_payment_type(sender)
    }}

for i in range(100):

    data = generate_receiver_transaction(random.randint(1, 3))
    print(data)