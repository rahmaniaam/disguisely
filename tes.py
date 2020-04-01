import pika

credentials = pika.PlainCredentials('0806444524', '0806444524')
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                        host='152.118.148.95',
                                        port=5672,
                                        virtual_host='/0806444524'))
channel = connection.channel()
channel.exchange_declare(exchange='1606828702', exchange_type='direct')
queue_result = channel.queue_declare(queue='key', durable=True)
channel.queue_bind(exchange='1606828702', queue=queue_result.method.queue)

channel.basic_publish(
                exchange='1606828702',
                routing_key='key',
                body=50)