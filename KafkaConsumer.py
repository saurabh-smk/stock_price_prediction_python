from confluent_kafka import Consumer
import boto3
import json


c = Consumer({
    'bootstrap.servers': 'xxxxx:9092',
    'group.id': 'mygroup2',
    'auto.offset.reset': 'latest'
})

c.subscribe(['testtopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    # print('Received message: {}'.format(msg.value().decode('utf-8')))
    x = msg.value().decode('utf-8')

    s3_client = boto3.client('s3')

    x = bytes(json.dumps(x).encode('UTF-8'))

    s3_client.put_object(Body=x, Bucket='xxx-xxxx', Key='stock-data')
    # print(x)

c.close()