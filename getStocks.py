import os
import requests
from app import app, db

def queryStocks():
    apiUrl = 'http://dev.markitondemand.com/Api/v2/Lookup/jsonp?input='
    results = {}
    errors = []
    try:
        response = requests.get(apiUrl+'a', timeout=2)
        # check response status code is valid (not 404)
        response.raise_for_status()
        responseJSON = response.json()
        print(responseJSON)
    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )
    return None
