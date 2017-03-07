import os
import requests
from app import db
from models import Stock

def queryStocks():
    print("Getting stocks")
    apiUrl = 'http://dev.markitondemand.com/Api/v2/Lookup/json?input='
    errors = []
    try:
        r = requests.get(apiUrl+'a', timeout=2)
        print(r.status_code)
        response = r.json()
        for stock in response:
            print(stock)
            insertStock(stock['Symbol'], stock['Name'], stock['Exchange'])
        print(db.query.all())
    except:
        print("Unable to get URL. Please make sure it's valid and try again.")
    return None

def insertStock(symbol, name, exchange):
    try:
        stock = Stock(symbol=symbol, name=name, exchange=exchange)
    except:
        print("Could not create Stock object")
    try:
        query = db.query.get(symbol)
    except:
        print("Could not get query")
    if query is None:
        db.session.add(stock)
        db.session.commit()
    else:
        symbol_equal = stock.symbol == query.symbol
        name_equal = stock.name == query.name
        exchange_equal = stock.exchange == query.exchange
        if symbol_equal is False or name_equal is False or exchange_equal is False:
            try:
                db.session.add(stock)
                db.session.commit()
            except:
                print("Unable to add item to database.")
        else:
            pass
    return None
