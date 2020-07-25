# from kafka import KafkaProducer
# from kafka.errors import KafkaError
#
# import json
# from faker import Faker
# import random
# from random import randint
# fake = Faker('en_US')
#
# for _ in range(10):
#     my_dict = {'AGE':randint(0, 100), 'NAME':fake.name(), 'ADDRESS':fake.address()}
#
# producer = KafkaProducer(bootstrap_servers=["b-2.msktest.mukjoq.c7.kafka.us-east-1.amazonaws.com:9092"])
#
# def on_send_success(record_metadata):
#     print(record_metadata.topic)
#     print(record_metadata.partition)
#     print(record_metadata.offset)
#
# def on_send_error(excp):
#     log.error('I am an errback', exc_info=excp)
#     # handle exception
#
# while True:
#     record_metadata = producer.send('AWSKafkaTutorialTopic', b'msg').add_callback(on_send_success).add_errback(on_send_error)
#
# producer.flush()

# from confluent_kafka import Producer
# from faker import Faker
# import json
#
# p = Producer({'bootstrap.servers': '3.236.15.169:9092'})
#
# def delivery_report(err, msg):
#     """ Called once for each message produced to indicate delivery result.
#         Triggered by poll() or flush(). """
#     if err is not None:
#         print('Message delivery failed: {}'.format(err))
#     else:
#         print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
#
#
# fake = Faker('en_US')
#
# def gen_ran_data(i):
#     data = {}
#     data["ID"] = i
#     data["name"] = fake.name()
#     data["address"] = fake.address()
#     data["Email-ID"] = fake.safe_email()
#     return data
#
#
# for i in range(0, 1000):
#     x = json.dumps(gen_ran_data(i))
#     print(x)
#     p.poll(0)
#
#     # Asynchronously produce a message, the delivery report callback
#     # will be triggered from poll() above, or flush() below, when the message has
#     # been successfully delivered or failed permanently.
#     p.produce('testtopic', x.encode('utf-8'), callback=delivery_report)
#     # Wait for any outstanding messages to be delivered and delivery report
#     # callbacks to be triggered.
# p.flush()


from CollectStockData import CollectStockData

from confluent_kafka import Producer
# from faker import Faker
import json
import time
import sys

class KafkaProducer():

    def __init__(self):

        self.p = Producer({'bootstrap.servers': '3.214.215.150:9092'})
        # self.fake = Faker('en_US')
        # print("")

        self.sendData()



    def delivery_report(self,err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


    # def gen_ran_data(self,i):
    #     data = {}
    #     data["ID"] = i
    #     data["name"] = self.fake.name()
    #     data["address"] = self.fake.address()
    #     data["Email-ID"] = self.fake.safe_email()
    #     return data

    def getData(self):

        key_1 = '3FWDSWTJWM7W1JCR'
        stock_list_1 = ['AAPL', 'TSLA', 'GOOGL', 'FB', 'AMZN']
        collect_data_1 = CollectStockData(key_1, stock_list_1)
        stock_data1 =  collect_data_1.GetAPIDataFor15Mins()

        # key_2 = 'xxx'
        # stock_list_2 = ['NFLX', 'UBER', 'DBX', 'TWTR', 'LNKD']
        # collect_data_2 = CollectStockData(key_2, stock_list_2)
        # stock_data2 = collect_data_2.GetAPIDataFor15Mins()

        return stock_data1

    def sendData(self):

        # for i in range(0, 1000):
        #     x = json.dumps(self.en_ran_data(i))
        #     print(x)
        time_count = 0
        while True:
            stock_data1 = self.getData()

            stock_data = stock_data1

            for stock in stock_data:
                cur_stock = json.dumps(stock)
                if "AAPL" in cur_stock:
                    print(cur_stock)

                    self.p.poll(0)
                    response = self.p.produce('aapl-topic', cur_stock.encode('utf-8'), callback=self.delivery_report)
                    print(response)
                if "TSLA" in cur_stock:
                    print(cur_stock)

                    self.p.poll(0)
                    response = self.p.produce('tsla-topic', cur_stock.encode('utf-8'), callback=self.delivery_report)
                    print(response)
                if "GOOGL" in cur_stock:
                    print(cur_stock)

                    self.p.poll(0)
                    response = self.p.produce('googl-topic', cur_stock.encode('utf-8'), callback=self.delivery_report)
                    print(response)
                if "FB" in cur_stock:
                    print(cur_stock)

                    self.p.poll(0)
                    response = self.p.produce('fb-topic', cur_stock.encode('utf-8'), callback=self.delivery_report)
                    print(response)
                if "AMZN" in cur_stock:
                    print(cur_stock)

                    self.p.poll(0)
                    response = self.p.produce('amzn-topic', cur_stock.encode('utf-8'), callback=self.delivery_report)
                    print(response)

                # print(cur_stock)
                #
                # self.p.poll(0)
                # response = self.p.produce('testtopic', cur_stock.encode('utf-8'), callback=self.delivery_report)
                # print(response)

            self.p.flush()

            time.sleep(60)
            time_count += 1
            if time_count == 15:
                break

kp = KafkaProducer()
