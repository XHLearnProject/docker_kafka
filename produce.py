from confluent_kafka import Producer

# Kafka 集群的地址
bootstrap_servers = 'localhost:9192,localhost:9292,localhost:9392'

# 创建 Kafka 生产者
producer = Producer({
    'bootstrap.servers': bootstrap_servers,
    'api.version.request': True
})


# 发送消息到 Kafka 主题
def send_message(topic, message):
    producer.produce(topic, value=message)
    producer.flush()

while True:
    msg = input("> ")
    # 调用发送消息的函数
    send_message('demo', msg)

# 关闭 Kafka 生产者
producer.close()
