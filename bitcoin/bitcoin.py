import requests
import sys

try:
    try:
        bitn = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(responce.json())

except requests.RequestException:
    pass