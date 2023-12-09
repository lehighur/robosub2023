
from time import sleep
from pymavlink import mavutil


gain = 1
depthHoldGain = .675
vectors = {
   'fore' : [int(0+1000*gain),0,int(500-500*depthHoldGain),0,0],
   'back' : [int(0-1000*gain),0,int(500-500*depthHoldGain),0,0],
    'right' : [0,int(0+1000*gain),int(500-500*depthHoldGain),0,0],
    'left' : [0,int(0-1000*gain),int(500-500*depthHoldGain),0,0],
    'up' : [0,0,int(500+500*gain),0,0],
    'down' : [0,0,int(500-500*gain),0,0],
    'turnRight' : [0,0,int(500-500*depthHoldGain),int(0+1000*gain),0],
    'turnLeft' : [0,0,int(500-500*depthHoldGain),int(0-1000*gain),0],
    'halt' :[0,0,int(500-500*depthHoldGain),0,0]
    }

def setupDrone():
    global drone
    #Connecting to Pixhawk
    print('Heartbeating Pixhawk...')
    drone = mavutil.mavlink_connection("/dev/ttyACM0", baud=115200)
    drone.wait_heartbeat()

    #Arm drone
    print('Arming Drone...')
    drone.mav.command_long_send(
        drone.target_system,
        drone.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
        0, #Confirmation
        1, #Params (1 - 7)
        0, 0, 0, 0, 0, 0
    )


def getCompassHeading():
    msg = drone.recv_match(type = 'VFR_HUD')
    while msg == None:
        msg = drone.recv_match(type = 'VFR_HUD')
        sleep(0.1)
		
    vfr = msg.to_dict()
    return vfr['heading']

def move(direction,duration=0):
    print(f'Moving {direction}wards for {duration} seconds.')
    i = 0
    while i <= duration :
        drone.mav.manual_control_send(drone.target_system,*vectors[direction])
        if duration-i<1:
            sleep(duration)
        else:
            sleep(1)
        i+=1
    if duration != 0:
        print(f'Done moving {direction}wards')


gateDuration = 30 #seconds
compassThreshold = 5


def setHeading(desiredHeading, duration = 0, seek=False):
    currentHeading = getCompassHeading()
    print(currentHeading)
    distanceTracker = 0
    while distanceTracker < duration and seek==True:
        currentHeading = getCompassHeading()
        if desiredHeading - currentHeading > compassThreshold:
            move('turnRight')
        elif desiredHeading - currentHeading < -compassThreshold: 
            move('turnLeft')
        else:
            move('forward')
            distanceTracker += .1
        sleep(.1)
    while abs(desiredHeading - currentHeading) > compassThreshold and seek == False:
        currentHeading = getCompassHeading()
        if desiredHeading - currentHeading > compassThreshold:
            move('turnRight')
        elif desiredHeading - currentHeading < -compassThreshold: 
            move('turnLeft')
    #print("Successfully Reached %d (%d)" %desiredHeading, currentHeading())
    print(f'Successfuly reached {desiredHeading}({currentHeading}) degrees')


setupDrone()
setupDrone()
sleep(10)

setHeading(90,duration=5, seek=True)
move('halt', 3)

