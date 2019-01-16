import pika

def sendMessage(msgQueue,msg):

# The first thing we need to do is to establish a connection with RabbitMQ server.
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel() 
# We are now connected to Rabbitmq server on localhost 

# Let's create a hello queue to which the message will be delivered:
    channel.queue_declare(queue='patientIDSend')
    channel.queue_declare(queue='acknowledge')

# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# Message to send: "msg" to queue: "msgQueue",
# The queue name needs to be specified in the 'routing_key' parameter and message in the 'body' paramater
    channel.basic_publish(exchange='',routing_key=msgQueue,body=msg)
    print("Message: ",msg," to Queue: ", msgQueue)
#Flush the the buffer to the queue
    connection.close()
