# Imports go at the top
from microbit import *
from pca9685 import *
import radio

pca = PCA9685()

altitude = 0
vel_azimuth = 0

while True:
    msg = radio.receive()
    if msg is not None: # Hey, Python: Please stop protecting me from myself! :p
        altitude = int(msg[0:3])
        vel_azimuth = int(msg[3:6])
        
        pca.setServoDegrees(1,altitude)
        if vel_azimuth > 10:
            pca.startStepper(1, False)
        elif vel_azimuth < -10:
            pca.startStepper(1, True)
        else:
            pca.stopStepper(1)
    sleep(50)
            