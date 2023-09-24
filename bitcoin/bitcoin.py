import requests
import sys

try:
    bitn = sys.argv[1]
    responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(responce.json())
    
except requests.RequestException:
    pass