import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')


# Country endpoint
def get_countries():
    response = requests.get('https://api.smspool.net/country/retrieve_all')

    if response.status_code == 200:
        data = json.loads(response.text)
        with open('./data/countries.txt', 'w') as f:
            f.write("{:<5} {:<25} {:<10} {:<15}\n".format(
                'ID', 'Country', 'Short Name', 'Region'))
            f.write("-" * 65 + "\n")
            for item in data:
                f.write("{:<5} {:<25} {:<10} {:<15}\n".format(
                    item['ID'], item['name'], item['short_name'], item['region']))
    else:
        print(f"Error: {response.status_code}")


# Service endpoint
def get_services():
    response = requests.get('https://api.smspool.net/service/retrieve_all')

    if response.status_code == 200:
        data = json.loads(response.text)
        with open('./data/services.txt', 'w') as f:
            f.write("{:<5} {:<25}\n".format('ID', 'Name'))
            f.write("-" * 35 + "\n")
            for item in data:
                f.write("{:<5} {:<25}\n".format(item['ID'], item['name']))
    else:
        print(f"Error: {response.status_code}")


# TODO: Balance endpoint
# TODO: Order history endpoint
# My active orders endpoint
def active_orders():
    url = "https://api.smspool.net/request/active"
    params = {
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        orders = response.json()
        pending_orders = [
            order for order in orders if order["status"] == "pending"]
        for order in pending_orders:
            print("Timestamp: ", order["timestamp"])
            print("Order Code: ", order["order_code"])
            print("Phone Number: ", order["phonenumber"])
            print("Code: ", order["code"])
            print("Full Code: ", order["full_code"])
            print("Short Name: ", order["short_name"])
            print("Service: ", order["service"])
            print("Status: ", order["status"])
            print("Expiry: ", order["expiry"])
            print("-" * 20)
    else:
        print("Error retrieving active orders.")
# TODO: Price endpoint
