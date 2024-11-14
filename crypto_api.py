# crypto_api.py
import requests

def get_crypto_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        
        # Extracting the USD price from the response
        usd_price = data["bpi"]["USD"]["rate_float"]
        return usd_price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")
        return None
