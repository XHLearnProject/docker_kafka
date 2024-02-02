from confluent_kafka import Consumer, KafkaError

# Kafka 集群的地址
bootstrap_servers = 'localhost:9192,localhost:9292,localhost:9392'

# 创建 Kafka 消费者
consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
})

# 订阅 Kafka 主题
consumer.subscribe(['demo'])

# 消费消息
while True:
    message = consumer.poll(1.0)

    if message is None:
        continue

    # if message.error():
    #     if message.error().code() == KafkaError._PARTITION_EOF:
    #         # 当达到分区末尾时，继续下一个消息
    #         print('Error1: {}'.format(message.error()))
    #         continue
    #     else:
    #         # 处理其他错误
    #         print('Error2: {}'.format(message.error()))
    #         continue

    # 处理接收到的消息
    print('Received message: {}'.format(message.value().decode('utf-8')))

# 关闭 Kafka 消费者
consumer.close()
