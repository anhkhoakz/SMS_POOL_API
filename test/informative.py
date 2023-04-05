import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variable with default value
api_key = os.getenv('api_key', None)

# Country endpoint
def get_countries(country=None):
    url = 'https://api.smspool.net/country/retrieve_all'
    params = {'country': country}
    response = requests.get(url, params=params)
    return response.json()

# Service endpoint
def get_services(country=None):
    url = 'https://api.smspool.net/service/retrieve_all'
    params = {'country': country}
    response = requests.get(url, params=params)
    return response.json()

# Balance endpoint
def get_balance():
    url = 'https://api.smspool.net/request/balance'
    params = {'key': api_key}
    response = requests.get(url, params=params)
    return response.json()

# Order history endpoint
def get_order_history():
    url = 'https://www.api.smspool.net/request/history'
    params = {'key': api_key}
    response = requests.get(url, params=params)
    return response.json()

# My active orders endpoint
def get_active_orders():
    url = 'https://api.smspool.net/request/active'
    params = {'key': api_key}
    response = requests.get(url, params=params)
    return response.json()

# Price endpoint
def get_price(country, service):
    url = 'https://api.smspool.net/request/price'
    params = {'key': api_key, 'country': country, 'service': service}
    response = requests.get(url, params=params)
    return response.json()

countries = get_countries()
print(countries)

services = get_services(country='US')
print(services)

balance = get_balance()
print(balance)

order_history = get_order_history()
print(order_history)

active_orders = get_active_orders()
print(active_orders)

price = get_price(country='US', service='1688')
print(price)
