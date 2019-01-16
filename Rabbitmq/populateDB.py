from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createDB import Base, Patient_Vitals,Patient_Registration
 
# create engine for the database
engine = create_engine('sqlite:///../Rabbitmq/Patient_Details.db')
# Binds metadata of the base class with the Patient_Details' engine
Base.metadata.bind = engine
# creates a session which is associated with cureent DB engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

i=10000
patient1 = Patient_Registration(patientID=1,name= "Ayush Gaurav",height=175,address="XYZ 123456" ,contact= 1234567890,sex= 'M' ,age= 22 ,email= "test@gmail.com")
i+=1
patient2 = Patient_Registration(patientID=2,name= "Divya Sharma",height=155,address="PQR 123456" ,contact= 7890123456,sex= 'F',age= 21 ,email= "test@gmail.com")
i+=1
patient3 = Patient_Registration(patientID=3,name= "Rohan Patil" ,height=173,address="ABC 123456" ,contact= 6789012345,sex= 'M' ,age= 24 ,email= "test@gmail.com" )


session.add(patient1)
session.add(patient2)
session.add(patient3)
session.commit()

patient1_vitals = Patient_Vitals(patient=patient1,bloodPresure="110/70",heartRate=89,SPo2=97,Temp=98,Allergies=None,prescribeTest= None,prescribeScan= None ) 
session.add(patient1_vitals)
session.commit()

patient1_vitals = Patient_Vitals(patient=patient2,bloodPresure="120/70",heartRate=89,SPo2=94,Temp=98,Allergies="Peanuts",prescribeTest= None,prescribeScan= None ) 

session.add(patient1_vitals)
session.commit()

patient1_vitals = Patient_Vitals(patient=patient3,bloodPresure="100/70",heartRate=89,SPo2=97,Temp=98,Allergies=None,prescribeTest= None,prescribeScan= None ) 
session.add(patient1_vitals)
session.commit()



patient1_vitals = Patient_Vitals(patient=patient1,bloodPresure="140/90",heartRate=102,SPo2=91,Temp=100,Allergies=None,prescribeTest= None,prescribeScan= "X-Ray" ) 
session.add(patient1_vitals)
session.commit()


patient1_vitals = Patient_Vitals(patient=patient1,bloodPresure="140/90",heartRate=102,SPo2=91,Temp=100,Allergies=None,prescribeTest= None,prescribeScan= "X-Ray" ) 
session.add(patient1_vitals)
session.commit()


patient1_vitals = Patient_Vitals(patient=patient1,bloodPresure="140/90",heartRate=102,SPo2=91,Temp=100,Allergies=None,prescribeTest= None,prescribeScan= "X-Ray" ) 
session.add(patient1_vitals)
session.commit()


patient1_vitals = Patient_Vitals(patient=patient1,bloodPresure="140/90",heartRate=102,SPo2=91,Temp=100,Allergies=None,prescribeTest= None,prescribeScan= "X-Ray" ) 
session.add(patient1_vitals)
session.commit()


patient1_vitals = Patient_Vitals(patient=patient1,bloodPresure="140/90",heartRate=102,SPo2=91,Temp=100,Allergies=None,prescribeTest= None,prescribeScan= "X-Ray" ) 
session.add(patient1_vitals)
session.commit()

patient1_vitals = Patient_Vitals(patient=patient2,bloodPresure="100/60",heartRate=72,SPo2=96,Temp=98,Allergies="Peanuts",prescribeTest= None,prescribeScan= "X-Ray" ) 
session.add(patient1_vitals)
session.commit()

