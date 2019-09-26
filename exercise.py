import requests

url = "https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json"

countries = requests.get(url).json()
# print(countries)

gov_url = countries[38]['legislatures'][0]['popolo_url']
print(gov_url)

gov_data = requests.get(gov_url).json()
