import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime,UniqueConstraint,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
# Construct a base class for declarative class definitions.
# to produces appropriate Table objects and makes the appropriate mapper() calls.
Base = declarative_base()
 
class Patient_Registration(Base):
    
    __tablename__ = 'Patient_Registration'
    patientID=Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    name=Column(String(250), nullable=False)
    address=Column(String(500), nullable=False)
    height=Column(Integer, nullable=False)
    contact=Column(Integer, nullable=False)
    sex=Column(String(2),nullable=False)
    age=Column(Integer)
    email=Column(String(250), nullable=False)
    
class Patient_Vitals(Base):
    __tablename__ = 'Patient_Vitals'
    id=Column(Integer, primary_key=True, autoincrement=True)
    patientID=Column(Integer,ForeignKey("Patient_Registration.patientID"),nullable=False)
    patient=relationship("Patient_Registration")
    date_time=Column(DateTime, default=func.now())
    bloodPresure=Column(String(7))
    heartRate=Column(Integer)
    SPo2=Column(Integer)
    Temp=Column(Integer)
    Allergies=Column(String(500))
    prescribeTest=Column(String(500))
    prescribeScan=Column(String(500))

engine = create_engine('sqlite:///../Rabbitmq/Patient_Details.db')
Base.metadata.create_all(engine)