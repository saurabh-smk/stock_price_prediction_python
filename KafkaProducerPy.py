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

from confluent_kafka import Producer
from faker import Faker
import json

p = Producer({'bootstrap.servers': '3.236.15.169:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


fake = Faker('en_US')

def gen_ran_data(i):
    data = {}
    data["ID"] = i
    data["name"] = fake.name()
    data["address"] = fake.address()
    data["Email-ID"] = fake.safe_email()
    return data


for i in range(0, 1000):
    x = json.dumps(gen_ran_data(i))
    print(x)
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('testtopic', x.encode('utf-8'), callback=delivery_report)
    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
p.flush()