# -*- coding: utf-8 -*-
`
"""User class to generate API access to candles.""" 


class User1():
    client = API(access_token=userVals.key)
    o = instruments.InstrumentsCandles(instrument=userVals.pair, params=userVals.params)


"""Getting candle data values.""" 


class CandleLogic:
    def OHLC(self, data):
        user1.client.request(user1.o)
        candles = user1.o.response.get("candles")
        # Getting More Data
        candleData = candles[data].get("mid")
        
        # Basic variables as below don't scale well 
        o = candleData.get("o")
        h = candleData.get("h")
        l = candleData.get("l")
        c = candleData.get("c")

        return float(o), float(h), float(l), float(c)

    
    def Open(self, data):
        return self.OHLC(data)[0]


"""Calling OHLC data."""


def High(self, data):
        return self.OHLC(data)[1]

def Low(self, data):
        return self.OHLC(data)[2]

def Close(self, data):
        return self.OHLC(data)[3]


"""Getting individual user data.""" 


def getData(self):
        numList = []
        for x in range(0, userVals.count):
            numList.append(self.Close(x))
        return numList
