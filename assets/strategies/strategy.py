# -*- coding: utf-8 -*-


"""Logic that controls trading strategies.""" 


class StrategyLogic():

    def SMA(self, prices, length, period):
        sum(prices[(length-period):length]) / period
    # Below for previous candle's SMA 
    def SMAprev(self, prices, length, period):
        sum(prices[(length-period-1):length-1]) / period
