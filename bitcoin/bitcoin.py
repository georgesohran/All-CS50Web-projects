import requests
import sys

try:
    bitn = sys.argv[1]
    requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

except requests.RequestException:
    ...