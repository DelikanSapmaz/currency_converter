import requests
from difflib import get_close_matches as match
url='https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()
data1 = data['rates']
firs_currency = input("first currency:")
second_currency = input("second currency:")
def currency():
    pass
print(data1[firs_currency],data1[second_currency])