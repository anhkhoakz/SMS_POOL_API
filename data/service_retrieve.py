import requests
import json

response = requests.get('https://api.smspool.net/service/retrieve_all')

if response.status_code == 200:
    data = json.loads(response.text)
    with open('services.txt', 'w') as f:
        f.write("{:<5} {:<25}\n".format('ID', 'Name'))
        f.write("-" * 35 + "\n")
        for item in data:
            f.write("{:<5} {:<25}\n".format(item['ID'], item['name']))
else:
    print(f"Error: {response.status_code}")
