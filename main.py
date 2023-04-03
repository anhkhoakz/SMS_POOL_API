import requests
import pyperclip
from config import *


def purchase_sms(api_key, country_code, service_id):
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

    pyperclip.copy(data.get('order_id'))


def active_orders(api_key):
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


def check_sms(api_key, order_id):
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


def cancel_sms(api_key, order_id):
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


if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Purchase SMS")
        print("2. My active orders endpoint")
        print("3. Check SMS status")
        print("4. Cancel SMS")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            purchase_sms(api_key, 1, 671)
        elif choice == "2":
            active_orders(api_key)
        elif choice == "3":
            order_id = input("Enter Order ID: ")
            check_sms(api_key, order_id)
        elif choice == "4":
            order_id = input("Enter Order ID: ")
            cancel_sms(api_key, order_id)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
