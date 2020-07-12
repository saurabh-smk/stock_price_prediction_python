#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 02:12:23 2020

@author: anikts
"""
from alpha_vantage.timeseries import TimeSeries

class CollectStockData:
    def __init__(self, key, stock_list):
        self.key = key
        self.stock_list = stock_list
        self.stock_data = [{}, {}, {}, {}, {}]

    def GetAPIDataFor15Mins(self):
        time_count = 0
        # while True:
        ts = TimeSeries(key=self.key, output_format='json')

        stock1_data, meta_data1 = ts.get_intraday(symbol=self.stock_list[0], interval='1min', outputsize='full')
        stock2_data, meta_data2 = ts.get_intraday(symbol=self.stock_list[1], interval='1min', outputsize='full')
        stock3_data, meta_data3 = ts.get_intraday(symbol=self.stock_list[2], interval='1min', outputsize='full')
        stock4_data, meta_data4 = ts.get_intraday(symbol=self.stock_list[3], interval='1min', outputsize='full')
        stock5_data, meta_data5 = ts.get_intraday(symbol=self.stock_list[4], interval='1min', outputsize='full')

        self.stock_data[0][self.stock_list[0]] = stock1_data
        self.stock_data[1][self.stock_list[1]] = stock2_data
        self.stock_data[2][self.stock_list[2]] = stock3_data
        self.stock_data[3][self.stock_list[3]] = stock4_data
        self.stock_data[4][self.stock_list[4]] = stock5_data

        # time.sleep(60)
        # time_count += 1
        # if time_count == 15:
        #     break

        return self.stock_data


if __name__ == "__main__":
    # execute only if run as a script
    stock_list_1 = ['AAPL', 'TSLA', 'GOOGL', 'FB', 'AMZN']
    key_1 = '3FWDSWTJWM7W1JCR'
    stock_data = CollectStockData(key_1, stock_list_1)
    stock_data.GetAPIDataFor15Mins()
    print("In main")
