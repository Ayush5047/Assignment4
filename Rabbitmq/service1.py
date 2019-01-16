from send import sendMessage
#from microservice1 import receivedACK


def sendToIDQueue(patientID):
    sendMessage("patientIDSend", patientID)