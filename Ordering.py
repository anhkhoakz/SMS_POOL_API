import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')


# Order SMS endpoint


def purchase_sms(country_code, service_id):
    url = "https://api.smspool.net/purchase/sms"

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

# Check SMS endpoint


def check_sms(order_id):
    url = "https://api.smspool.net/sms/check"

    payload = {
        "key": api_key,
        "orderid": order_id,
    }

    response = requests.post(url, data=payload)

    if response.ok:
        data = response.json()
        status = data.get("status")
        message = data.get("message")
        sms = data.get("sms")
        full_sms = data.get("full_sms")
        resend = data.get("resend")
        expiration = data.get("expiration")

        if status == 1:
            print("SMS status: Pending")
        elif status == 2:
            print("SMS status: Expired")
        elif status == 3:
            print(f"SMS status: Received\nSMS content: {full_sms}")
        elif status == 4:
            print("SMS status: Resend requested")
        elif status == 5:
            print("SMS status: Cancelled")
        elif status == 6:
            print("SMS status: Refunded")
        else:
            print("Unknown SMS status")

        print(f"Message: {message}")
        print(f"SMS code: {sms}")
        print(f"Resend count: {resend}")
        print(f"Expiration: {expiration}")
    else:
        print(f"Failed to connect to {url}! Error: {response.status_code}")

# TODO: Resend SMS endpoint


# Cancel SMS endpoint
def cancel_sms(order_id):
    import requests
    url = "https://api.smspool.net/sms/cancel"

    params = {
        "key": api_key,
        "orderid": order_id
    }

    response = requests.post(url, data=params)
    if response.status_code == 200:
        result = response.json()
        if result["success"] == 1:
            print("SMS cancellation successful!")
        else:
            print("SMS cancellation failed.")
    else:
        print("Failed to connect to the SMSPOOL API.")

# TODO: Archive SMS orders endpoint
