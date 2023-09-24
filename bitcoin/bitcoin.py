import requests
import sys

try:
    try:
        bitn = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    price = responce["bpi"]["USD"]["rate_float"]
    print(f"${price*bitn:,.4f}")

except requests.RequestException:
    sys.exit("Error")