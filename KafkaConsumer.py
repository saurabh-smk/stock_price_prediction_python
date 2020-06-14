from confluent_kafka import Consumer


c = Consumer({
    'bootstrap.servers': '3.229.142.183:9092',
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

    print(x)

c.close()