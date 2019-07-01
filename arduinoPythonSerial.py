import serial  # Import the Serial Library

arduinoSerialData = serial.Serial('COM4', 9600)

while 1 == 1:
    if arduinoSerialData.inWaiting() > 0:
        myData = arduinoSerialData.readline()
        print (myData)