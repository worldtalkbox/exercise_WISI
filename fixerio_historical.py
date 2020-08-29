import datetime
import json
import requests


today = datetime.date.today()
amounts = 0
fromCurrency = ""
toCurrency = ""

# getRate() is the counting function with input amounts from currency to currency.
# If you input wrong KEY (currency), then return 0, otherwise return exchanged currency amounts.
def getRate(amounts, fromCurrency, toCurrency):
    with open("fixerio_dates.json", "r") as json_file:
        fixerio_file = json.load(json_file)

    try:
        fromD = fixerio_file['rates' ][fromCurrency]
        toD = fixerio_file['rates'][toCurrency]
        if (amounts <= 0):
            return 0
        else:
            return amounts * toD * (1/fromD)
    except KeyError:
        return 0

# setTodayRate() is get 'Currency Exchange Rates' from fixer.io
# The information is stored with JSON file if that is new one.
def setTodayRate():
    API_KEY = '8ea5952b526efd8fcd03e9723ff5b67c'
    url = 'http://data.fixer.io/api/latest?access_key=' + API_KEY
    response = requests.get(url=url)
    fixerio_data = response.json()

    if (fixerio_data["date"] >= str(today) ):
        with open("fixerio_dates.json", "w") as json_file:
            json.dump(fixerio_data, json_file)



setTodayRate()

ans = 'y'
while (ans == 'y' or ans == 'Y'):
    amounts = int(input('Input Amounts >> '))
    fromCurrency = str(input('From Currency >> ')).upper()
    toCurrency = str(input('To Currency >> ')).upper()

    print(str(amounts) + " " + fromCurrency + " => "  + str( format( getRate(amounts, fromCurrency, toCurrency), '.2f')) + " " + toCurrency)
    print()
    print('If you want to continue, please input key : y or Y  ')
    ans = str(input('input >> '))





