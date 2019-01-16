import pika
from service2 import callService2
from service3 import callService3

#The first thing we need to do is to establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel() 
#We are now connected to Rabbitmq server on localhost 

#Creating two queues for send patientId and Acknowledge
#Although it is not necessary to create the same queue byt when receive.py is called before send.py we will get an error
channel.queue_declare(queue='patientIDSend')
channel.queue_declare(queue='acknowledge')


#Whenever we receive a message, this callback function is called by the Pika library.
def callbackId(ch, method, properties, body):
    print(" [x] Received patientID %r" % body)
    b = str(body, 'utf-8')
    callService2(body)
#Tells RabbitMQ that this particular callback function should receive messages from patientIDSend queue

def callingCallbackId():
    channel.basic_consume(callbackId,queue='patientIDSend',no_ack=True)
    print(' [*] Waiting for messages in patientIDSend. To exit press CTRL+C')

#Whenever we receive a message, this callback function is called by the Pika library.
def callbackAck(ch, method, properties, body):
    print(" [x] Received Acknowledge %r" % body)
    b = str(body, 'utf-8')
    callService3(body)
#Tells RabbitMQ that this particular callback function should receive messages from acknowledge queue

def callingCallbackAck():
    channel.basic_consume(callbackAck,queue='acknowledge',no_ack=True)
    print(' [*] Waiting for messages in Acknowledge. To exit press CTRL+C')


if __name__ == '__main__':
    callingCallbackId()
    callingCallbackAck()
#It is a never-ending loop that waits for data and runs callbacks whenever necessary.
    channel.start_consuming()
