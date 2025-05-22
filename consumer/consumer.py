import pika

def callback(ch, method, properties, body):
    print(f'Received: {body.decode()}')

connection = pika.BlockingConnection(pika.ConnectionParameters(host= 'localhost'))
channel = connection.channel()
queue = 'messages'
channel.queue_declare(queue=queue, durable=True)
channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
print('Aguardando mensagens')
channel.start_consuming() 