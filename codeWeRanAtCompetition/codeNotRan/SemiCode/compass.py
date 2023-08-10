from pymavlink import mavutil
from time import sleep
import setup
def getCompassHeading():
    msg = drone.recv_match(type = 'VFR_HUD')
    while msg == None:
        msg = drone.recv_match(type = 'VFR_HUD')
        sleep(0.1)
		
    vfr = msg.to_dict()
    return vfr['heading']


global gateDuration 
global compassThreshold

def setHeading(desiredHeading, duration = 0, seek=False):
    currentHeading = getCompassHeading()
    print(str(currentHeading))
    distanceTracker = 0
    while distanceTracker < duration and seek==True:
        currentHeading = getCompassHeading()
        
        if desiredHeading - currentHeading > compassThreshold:
            move('turnRight')
        elif desiredHeading - currentHeading < -compassThreshold:
            move('turnLeft')
        else:
            move('fore')
            distanceTracker += .1
        sleep(.1)
    while abs(desiredHeading - currentHeading) > compassThreshold and seek == False:

        currentHeading = getCompassHeading()
        if desiredHeading - currentHeading > compassThreshold:
            move('turnRight')
        elif desiredHeading - currentHeading < -compassThreshold:
            move('turnLeft')
    #print("Successfully Reached %d (%d)" %desiredHeading, currentHeading())
    print(f'Successfuly reached {desiredHeading}({currentHeading}) degrees\n')

