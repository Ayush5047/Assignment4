from flask import Flask, request, jsonify, make_response
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from microservice1 import session
import sys
from send import sendMessage
import random
import json
sys.path.insert(0, '../Database')
from createDB import Base, Patient_Registration, Patient_Vitals


def callService2(body):
    
    received = body
    e = json.loads(received.decode('utf-8'))
    if(session.query(Patient_Registration).filter(Patient_Registration.patientID == e['patientID']).first() is not None):
        e['ack']='Yes'
    else:
        e['ack']='No'
    
    e1 = json.dumps(e)
    sendMessage("acknowledge",e1)