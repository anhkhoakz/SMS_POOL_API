import requests
from config import *

url = "https://api.smspool.net/purchase/sms"
country_code = 1
service_id = 671

payload = {
    "key": api_key,
    "country": country_code,
    "service": service_id,
}

response = requests.post(url, data=payload)

if response.ok:
    data = response.json()
    if data.get("success") == 1:
        print("SMS order placed successfully!")
        print(f"Number: {data.get('number')}")
        print(f"Order ID: {data.get('order_id')}")
        print(f"Country: {data.get('country')}")
        print(f"Service: {data.get('service')}")
        print(f"Pool: {data.get('pool')}")
        print(f"Expires in: {data.get('expires_in')} seconds")
        print(f"Message: {data.get('message')}")
    else:
        print("SMS order failed!")
        print(f"Error message: {data.get('message')}")
else:
    print(f"Failed to connect to {url}! Error: {response.status_code}")
