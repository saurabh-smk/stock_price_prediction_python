#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 02:12:23 2020

@author: anikts
"""
from alpha_vantage.timeseries import TimeSeries
from datetime import date

class CollectStockData:

    '''
    'self.key': Alpha vantage key to get the response of the 'get_intraday' API.
    'self.stock_list': to get the list of the current stocks.
    'self.stock_data': to get the share details, key of each dictionary is the share name.
    '''
    def __init__(self, key, stock_list):
        self.key = key
        self.stock_list = stock_list
        self.stock_data = [{}, {}, {}, {}, {}]

    '''
    Method to call intraday Alpha Vantage API to collect last 5 days full data with 1 minute interval
    '''
    def GetAPIDataFor15Mins(self):
        ts = TimeSeries(key=self.key, output_format='json')

        stock1_data, meta_data1 = ts.get_intraday(symbol=self.stock_list[0], interval='1min', outputsize='compact')
        stock2_data, meta_data2 = ts.get_intraday(symbol=self.stock_list[1], interval='1min', outputsize='compact')
        stock3_data, meta_data3 = ts.get_intraday(symbol=self.stock_list[2], interval='1min', outputsize='compact')
        stock4_data, meta_data4 = ts.get_intraday(symbol=self.stock_list[3], interval='1min', outputsize='compact')
        stock5_data, meta_data5 = ts.get_intraday(symbol=self.stock_list[4], interval='1min', outputsize='compact')

        self.stock_data[0][self.stock_list[0]] = stock1_data
        self.stock_data[1][self.stock_list[1]] = stock2_data
        self.stock_data[2][self.stock_list[2]] = stock3_data
        self.stock_data[3][self.stock_list[3]] = stock4_data
        self.stock_data[4][self.stock_list[4]] = stock5_data

        f = open('sample_data123.txt', 'w')
        f.write('dict = ' + repr(self.stock_data) + '\n')
        f.close()

        # self.stock_data = self.preprocessStockData()

        # print(self.stock_data)
        # f = open('stock_data_sample_data.py', 'w')
        # f.write('dict = ' + repr(self.stock_data) + '\n')
        # f.close()

        return self.stock_data

    '''
    Method to preprocess the response of the API, as API provides last 5 days data, using this function only current days
    data is fetched.
    '''
    def preprocessStockData(self):
        # today = date.today()
        today = '2020-07-10'
        processed_stocks =[{},{},{},{},{}]
        for share in range(len(self.stock_list)):
            for key,value in self.stock_data[share][self.stock_list[share]].items():
                if today in key:
                    processed_stocks[share][key] = value

        f = open('sample_data.txt', 'w')
        f.write('dict = ' + repr(processed_stocks) + '\n')
        f.close()
        return processed_stocks

    
    
if __name__ == "__main__":
    # execute only if you want to this file as a script to get stock_data
    # stock_list_1 = ['AAPL', 'TSLA', 'GOOGL', 'FB', 'AMZN']
    # key_1 = 'xxxxxx'
    # stock_data = CollectStockData(key_1, stock_list_1)
    # stock_data.GetAPIDataFor15Mins()
    #
    print("Completed fetching data of stocks")
