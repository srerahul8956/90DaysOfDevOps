import requests
import os
API_Key ="F8NYOXJD0ZT9YRR8"

apiurl = "https://www.alphavantage.co/"


def get_stock_price(symbol):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_Key}"
    response = requests.get(apiurl+query).json()

    for key,value in response.items():
        if key == "Time Series (Daily)":
            continue   # skip the loop at this point
        else:
            print(key, value)
                 

symbol = input("Enter the stock symbol (eg:AMZN, GOOGL, AAPL, IBM) \n: ")
get_stock_price(symbol)

