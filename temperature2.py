import serial
import RPi.GPIO as GPIO
import os, time  
from w1thermsensor import W1ThermSensor
from array import *
from json_tricks import dumps
import datetime

sensor = W1ThermSensor()
GPIO.setmode(GPIO.BOARD)

# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=5)

def warning():
    print("WARNING !! Temperature too high!!")
    time.sleep(1)
    port.write(('AT'+'\r\n').encode())
    time.sleep(1)
    port.write(('ATE0'+'\r').encode())      # Disable the Echo
    time.sleep(1)
    port.write(('AT+CMGF=1'+'\r').encode())  # Select Message format as Text mode 
    time.sleep(1)
    port.write(('AT+CNMI=2,1,0,0,0'+'\r').encode())   # New SMS Message Indications
    time.sleep(1)
    # Sending a message to a particular Number
         
    port.write(('AT+CMGS="+254726309019"'+'\r').encode())
    time.sleep(1) 
    port.write(('WARNING !! Temperature too high!!'+'\r').encode())  # Message
    time.sleep(1)
    port.write(("\x1A").encode()) # Enable to send SMS
    time.sleep(1)
    port.write(('ATD+254726309019;'+'\r').encode()) 
    time.sleep(1)
def get_temps():
    while True:
        data=[]
        now=datetime.datetime.now()
        temperature =(sensor.get_temperature())
        data.append({'temp':temperature,'date':now})
        print (dumps(data))
        while True:
                if (sensor.get_temperature())>=24:
                    warning()
                    print (dumps(data))
                    time.sleep(1)
                break
        while True:
                if (sensor.get_temperature())<=20:
                    warning()
                    print (dumps(data))
                    time.sleep(1)
                break


get_temps()


               
    
    
