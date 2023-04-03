import requests
from config import *

url = "https://api.smspool.net/sms/check"
order_id = "LSB9WJGR"

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
