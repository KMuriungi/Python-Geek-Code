import serial # Import the Serial Library
from visual import * # Import all the vPython libraries

arduinoSerialData = serial.Serial('COM4',9600) # Create an object to read serial port
measuringRod = cylinder(length = 10, color = color.blue, radius = .5, pos = (-3,0,0))
lengthLabel = label(text = 'Target Distance is: ', pos(0,1,0), height = 30, box = false)

while (1 == 1): # Loop forever
    rate(20)
    if (arduinoSerialData.inWaiting()>0): # Check to see if the data is on the serial port
        myData = arduinoSerialData.readline() #Ifdata is there, then read it.
        distance = float (myData) # Convert string myData to floating point number and hold in distance variable
        print distance
        myLabel ='Target Distance is: ' + myData
        lengthLebel.text = myLabel
        measuringRod.length = distance