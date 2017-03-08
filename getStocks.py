import os
import requests
from app import db
from models import Stock

def queryStocks():
    print("Getting stocks")
    apiUrl = 'http://dev.markitondemand.com/Api/v2/Lookup/json?input='
    results = {}
    errors = []
    try:
        r = requests.get(apiUrl+'d', timeout=2)
        print(r.status_code)
        response = r.json()
        for stock in response:
            insertStockInDB(stock['Symbol'], stock['Name'], stock['Exchange'])
    except:
        print("Unable to get URL. Please make sure it's valid and try again.")
    return None

def insertStockInDB(symbol, name, exchange):
    # Create stock object to be inserted into DB
    try:
        stock = Stock(symbol=symbol, name=name, exchange=exchange)
    except:
        print("Could not create Stock object")
    # Query DB to see if stock exists already
    try:
        query = db.session.query(Stock).filter_by(symbol=symbol).all()
    except (Exception) as e:
        print(e)
    # If symbol of stock not found try to add stock to DB
    if len(query) is 0:
        try:
            db.session.add(stock)
            db.session.commit()
        except:
            print("Unable to commit stock")
    # If symbol found check further that stock is not the same
    else:
        # Flag for existence of stock
        stockExists = False;
        # Check if stock of same name and exchange exists
        for result in query:
            name_equal = stock.name == result.name
            exchange_equal = stock.exchange == result.exchange
            if name_equal is True and exchange_equal is True:
                stockExists = True
                break
        # If stock does not exist then try to add stock to DB
        if stockExists is False:
            try:
                db.session.add(stock)
                db.session.commit()
            except:
                print("Unable to commit stock")
    return None
