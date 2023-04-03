import requests
import json

response = requests.get('https://api.smspool.net/country/retrieve_all')

if response.status_code == 200:
    data = json.loads(response.text)
    with open('countries.txt', 'w') as f:
        f.write("{:<5} {:<25} {:<10} {:<15}\n".format('ID', 'Country', 'Short Name', 'Region'))
        f.write("-" * 65 + "\n")
        for item in data:
            f.write("{:<5} {:<25} {:<10} {:<15}\n".format(item['ID'], item['name'], item['short_name'], item['region']))
else:
    print(f"Error: {response.status_code}")
