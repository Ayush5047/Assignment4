from flask import Flask, request, jsonify, make_response
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from service1 import sendToIDQueue
import json
import time
from createDB import Base, Patient_Registration, Patient_Vitals

global jsonData
global ackReceived
global ackRecievedUsed

ackReceived = ''
# ackReceivedUsed =True means ACK used
ackReceivedUsed = True
jsonData = {}

# create your flask application
app = Flask(__name__)
# create engine for the database
engine = create_engine('sqlite:///Patient_Details.db')
# Binds metadata of the base class with the Patient_Details' engine
Base.metadata.bind = engine
# creates a session which is associated with current DB engine
patientDetailsSession = sessionmaker(bind=engine)
session = patientDetailsSession()

def receivedACK(body):
    global ackReceived
    ackReceived=json.loads(body.decode('utf-8'))
    patientID=ackReceived['patientID']
    if(ackReceived['ack']=="Yes"):
            session.query(Patient_Registration).filter(Patient_Registration.patientID == patientID).update( {
            Patient_Registration.name : ackReceived['name']
            })
            session.commit()
       
    elif(ackReceived['ack']=="No"):
        print("Record not Found")
        # return jsonify('message:','Patient Not Found')
    global ackReceivedUsed
    ackReceivedUsed=False


@app.route('/patientupdate', methods=['POST', 'GET'])
def patientupdate():
    if request.method == 'POST':
# Get patient details in the form of JSON
        data1 = request.get_json()
        print(type(data1))
        data = json.dumps(data1)
        global jsonData
        jsonData = data
        # send patientID for checking through Rabbitmq
        sendToIDQueue(data)
        
        global ackReceivedUsed
        global ackReceived       
        
        return jsonify('user:', data)
        # waiting for acknowldge to come
        


if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost',port=5001)