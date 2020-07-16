from confluent_kafka import Consumer
import boto3
import json


aapl_consumer = Consumer({
    'bootstrap.servers': 'xxxxxx:9092',
    'group.id': 'stock-consumer-group',
    'auto.offset.reset': 'latest'
})

aapl_consumer.subscribe(['aapl-topic'])

tsla_consumer = Consumer({
    'bootstrap.servers': 'xxxxxx:9092',
    'group.id': 'stock-consumer-group',
    'auto.offset.reset': 'latest'
})

tsla_consumer.subscribe(['tsla-topic'])

googl_consumer = Consumer({
    'bootstrap.servers': 'xxxxxx:9092',
    'group.id': 'stock-consumer-group',
    'auto.offset.reset': 'latest'
})

googl_consumer.subscribe(['googl-topic'])

fb_consumer = Consumer({
    'bootstrap.servers': 'xxxxxx:9092',
    'group.id': 'stock-consumer-group',
    'auto.offset.reset': 'latest'
})

fb_consumer.subscribe(['fb-topic'])

amzn_consumer = Consumer({
    'bootstrap.servers': 'xxxxxx:9092',
    'group.id': 'stock-consumer-group',
    'auto.offset.reset': 'latest'
})

amzn_consumer.subscribe(['amzn-topic'])



while True:
    aapl_msg = aapl_consumer.poll(1.0)
    tsla_msg = tsla_consumer.poll(1.0)
    googl_msg = googl_consumer.poll(1.0)
    fb_msg = fb_consumer.poll(1.0)
    amzn_msg = amzn_consumer.poll(1.0)

    # if aapl_msg is None:
    #     continue
    # if tsla_msg is None:
    #     continue
    # if googl_msg is None:
    #     continue
    # if fb_msg is None:
    #     continue
    # if amzn_msg is None:
    #     continue

    # if aapl_msg.error():
    #     print("Consumer error: {}".format(aapl_msg.error()))
    #     continue
    # if tsla_msg.error():
    #     print("Consumer error: {}".format(tsla_msg.error()))
    #     continue
    # if googl_msg.error():
    #     print("Consumer error: {}".format(googl_msg.error()))
    #     continue
    # if fb_msg.error():
    #     print("Consumer error: {}".format(fb_msg.error()))
    #     continue
    # if aapl_msg.error():
    #     print("Consumer error: {}".format(aapl_msg.error()))
    #     continue

    if aapl_msg is not None:
        print('Received message from AAPL Topic: {}'.format(aapl_msg.value().decode('utf-8')))
    if tsla_msg is not None:
        print('Received message from TSLA Topic: {}'.format(tsla_msg.value().decode('utf-8')))
    if googl_msg is not None:
        print('Received message from GOOGL Topic: {}'.format(googl_msg.value().decode('utf-8')))
    if fb_msg is not None:
        print('Received message from FB Topic: {}'.format(fb_msg.value().decode('utf-8')))
    if amzn_msg is not None:
        print('Received message from AMZN Topic: {}'.format(amzn_msg.value().decode('utf-8')))

    # print('Received message from TSLA Topic: {}'.format(tsla_msg.value().decode('utf-8')))
    # print('Received message from GOOGL Topic: {}'.format(googl_msg.value().decode('utf-8')))
    # print('Received message from FB Topic: {}'.format(fb_msg.value().decode('utf-8')))
    # print('Received message from AMZN Topic: {}'.format(amzn_msg.value().decode('utf-8')))

    # x = amzn_msg.value().decode('utf-8')
    #
    # s3_client = boto3.client('s3')
    #
    # x = bytes(json.dumps(x).encode('UTF-8'))
    #
    # s3_client.put_object(Body=x, Bucket='zxcvcbdbx', Key='stock-data')
    # print(x)

# c.close()
# d.close()

aapl_consumer.close()
tsla_consumer.close()
googl_consumer.close()
fb_consumer.close()
amzn_consumer.close()