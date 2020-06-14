#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 02:12:23 2020

@author: anikts
"""
# from alpha_vantage.timeseries import TimeSeries
# import time
#
# class CollectStockData:
#     def __init__(self, key, stock_list):
#         self.key = key
#         self.stock_list = stock_list
#         self.stock_data = [{},{},{},{},{}]
#
#     def GetAPIDataFor15Mins(self):
#         time_count = 0
#         while True:
#             ts = TimeSeries(key=self.key, output_format='json')
#
#             stock1_data,meta_data1 = ts.get_intraday(symbol=self.stock_list[0],interval='1min', outputsize='full')
#             stock2_data,meta_data2 = ts.get_intraday(symbol=self.stock_list[1],interval='1min', outputsize='full')
#             stock3_data,meta_data3 = ts.get_intraday(symbol=self.stock_list[2],interval='1min', outputsize='full')
#             stock4_data,meta_data4 = ts.get_intraday(symbol=self.stock_list[3],interval='1min', outputsize='full')
#             stock5_data,meta_data5 = ts.get_intraday(symbol=self.stock_list[4],interval='1min', outputsize='full')
#
#             self.stock_data[0][meta_data1['3. Last Refreshed']] = stock1_data
#             self.stock_data[1][meta_data2['3. Last Refreshed']] = stock2_data
#             self.stock_data[2][meta_data3['3. Last Refreshed']] = stock3_data
#             self.stock_data[3][meta_data4['3. Last Refreshed']] = stock4_data
#             self.stock_data[4][meta_data5['3. Last Refreshed']] = stock5_data
#             print(self.stock_data)
#             time.sleep(60)
#             time_count+=1
#             if time_count == 15:
#                 break
#
# key_1 = 'E3789ZJ6PAOUYJ7J'
# stock_list_1 = ['AAPL','TSLA','GOOGL','FB','AMZN']
# collect_data_1 = CollectStockData(key_1, stock_list_1)
# collect_data_1.GetAPIDataFor15Mins()
#
# key_2 = '3FWDSWTJWM7W1JCR'
# stock_list_2 = ['NFLX','UBER','DBX','TWTR','LNKD']
# collect_data_2 = CollectStockData(key_2, stock_list_2)
# collect_data_2.GetAPIDataFor15Mins()



from alpha_vantage.timeseries import TimeSeries
# import time

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

        self.stock_data[0][meta_data1['3. Last Refreshed']] = stock1_data
        self.stock_data[1][meta_data2['3. Last Refreshed']] = stock2_data
        self.stock_data[2][meta_data3['3. Last Refreshed']] = stock3_data
        self.stock_data[3][meta_data4['3. Last Refreshed']] = stock4_data
        self.stock_data[4][meta_data5['3. Last Refreshed']] = stock5_data

        # time.sleep(60)
        # time_count += 1
        # if time_count == 15:
        #     break


        return self.stock_data


if __name__ == "__main__":
    # execute only if run as a script
    print("In main")
