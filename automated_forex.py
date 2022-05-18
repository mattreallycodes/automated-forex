# -*- coding: utf-8 -*-

# Oanda Packages
from oandapyV20 import API
import oandapyV20
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails 
from oandapyV20.contrib.requests import StopLossDetails
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.accounts as accounts


"""Class below generates universal variables for strategy, Oanda API."""


class UserVals():
    SMAbig = 50
    # More user values
    SMAsmall = 25
    count = 55
    key ="5d864f56f6584527cf9643baa356ebe2-70fe098f5c72b94604bb47996d2c6f27"
    accountID = "101-001-22369468-001"
    pair="EUR_USD"
    params = {
     "count": count,
     "granularity": "H4"
    }


