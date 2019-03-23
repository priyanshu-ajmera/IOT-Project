import RPi.GPIO as ha
import Adafruit_DHT as dht
ha.setmode(ha.BOARD)
ha.setwarning(False)
ha.setup(3,ha.IN)       #LDR Sensor
ha.setup(5,ha.OUT)      #Lights
ha.setup(7,ha.OUT)      #Curtains
ha.setup(12,ha.IN)      #LPG Sensor
ha.setup(13,ha.IN)      #IR Sensor
ha.setup(11,ha.OUT)     #Buzzer
ha.setup(15,ha.IN)      #Temp. Sensor
ha.setup(16,ha.OUT)     #Fan

while 1:
    if(ha.input(3)==1):             #Lights and Curtains
        ha.output(5,0)
        print("Lights OFF")
        ha.output(7,1)
        print("Curtains OPEN")
    else:
        ha.output(5,1)
        print("Lights ON")
        ha.output(7,0)
        print("Curtains CLOSE")
       

    if(ha.input(12)==1):            #LPG Sensor
        ha.output(11,1)
        print("Buzzer ON")
    else:
        ha.output(11,0)
        print("Buzzer OFF")

 
    if(ha.input(13)==1):            #IR Sensor
        ha.output(11,1)
        print("Buzzer ON")
    else:
        ha.output(11,0)
        print("Buzzer OFF")


    temp=dht.read_retry(11,22)      #Temperature
    if(ha.input(15)>25):
        ha.output(16,1)
        print("Fan ON")
    else:
        ha.output(16,0)
        print("Fan OFF")
    
