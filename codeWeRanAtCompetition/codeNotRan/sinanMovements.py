# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:36:08 2023

@author: Kitun
"""
import sys
sys.path.append("/usr/bin/python")
from time import sleep
from pymavlink import mavutil

import rclpy
from rclpy.node import Node
from ros2topic.api import get_msg_class

depthHoldGain = 0.5
gain = 0.5 # 0-1
vectors = {
   'fore' : [int(0+1000*gain),0,int(500-500*depthHoldGain),0,0],
   'back' : [int(0-1000*gain),0,int(500-500*depthHoldGain),0,0],
    'right' : [0,int(0+1000*gain),int(500-500*depthHoldGain),0,0],
    'left' : [0,int(0-1000*gain),int(500-500*depthHoldGain),0,0],
    'up' : [0,0,int(500+500*gain),0,0],
    'down' : [0,0,int(500-500*gain),0,0],
    'turnLeft' : [0,0,int(500-500*depthHoldGain),int(0+1000*gain),0],
    'turnRight' : [0,0,int(500-500*depthHoldGain),int(-1000*gain),0],
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


def move(direction,duration=-1):
    duration = float(duration)
    print(f'Moving {direction}wards')
    drone.mav.manual_control_send(drone.target_system,*vectors[direction])
    i = 0
    while (-i + duration) > 1:
        sleep(1)
        i+=1
        print(i)
        drone.mav.manual_control_send(drone.target_system, vectors[direction][0], vectors[direction][1], vectors[direction][2], vectors[direction][3], vectors[direction][4])
    sleep(duration - i)    
   # drone.mav.manual_control_send(drone.target_system, vectors['halt'][0], vectors['halt'][1], vectors['halt'][2], vectors['halt'][3], vectors['halt'][4])
    drone.mav.manual_control_send(drone.target_system, 0, 0, 500, 0, 0)
    changeFlightMode('STABILIZE')
    sleep(0.25)
    drone.mav.manual_control_send(drone.target_system, 0, 0, 500, 0, 0)
    changeFlightMode('MANUAL')
    print(f'Done moving {direction}wards')


def changeFlightMode(mode): #STABILIZE , DEPTHHOLD , MANUAL , ACRO
    print(f'Changing flight mode to {mode}')
    mode_id = drone.mode_mapping()[mode]
    drone.mav.command_long_send(
        drone.target_system, # Target system ID
        drone.target_component, # Target component ID
        mavutil.mavlink.MAV_CMD_DO_SET_MODE, # ID of command to send
        0,  # Confirmation
        0, 
        mode_id, 
        0, 
        0, 
        0, 
        0, 
        0)
    
def changeFlightMode2(mode):
    # Check if mode is available
    if mode not in drone.mode_mapping():
        print('Unknown mode : {}'.format(mode))
        print('Try:', list(drone.mode_mapping().keys()))
        sys.exit(1)
    
    # Get mode ID
    mode_id = drone.mode_mapping()[mode]
    # Set new mode
    # master.mav.command_long_send(
    #    master.target_system, master.target_component,
    #    mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
    #    0, mode_id, 0, 0, 0, 0, 0) or:
    # master.set_mode(mode_id) or:
    drone.mav.set_mode_send(
    drone.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode_id)

    while True:
        # Wait for ACK command
        # Would be good to add mechanism to avoid endlessly blocking
        # if the autopilot sends a NACK or never receives the message
        ack_msg = drone.recv_match(type='COMMAND_ACK', blocking=True)
        ack_msg = ack_msg.to_dict()

        # Continue waiting if the acknowledged command is not `set_mode`
        if ack_msg['command'] != mavutil.mavlink.MAV_CMD_DO_SET_MODE:
            continue

        # Print the ACK result !
        print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
        break

# Create a function to send RC values
# More information about Joystick channels
# here: https://www.ardusub.com/operators-manual/rc-input-and-output.html#rc-inputs
def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    drone.mav.rc_channels_override_send(
        drone.target_system,                # target_system
        drone.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.

def main(*ddPair):
    sleep(5)
    try:
        setupDrone()
        for item in sys.argv[2::]:
            item = item.split(',')
            item[1] = float(item[1])
            if(item[0] == "fore"):
                i = 0
                while(item[1] > i):
                    changeFlightMode2('MANUAL')
                    sleep(.5)
                    set_rc_channel_pwm(5, 1700)
                    changeFlightMode2('STABILIZE')
                    sleep(.5)
                    i += 1
            elif(item[0] == "down"):
                i = 0
                while(item[1] > i):
                    changeFlightMode2('MANUAL')
                    sleep(.5)
                    set_rc_channel_pwm(6, 1300)
                    changeFlightMode2('STABILIZE')
                    sleep(.5)
                    i += 1
            else:
                changeFlightMode2('MANUAL')
                move(*item)
    except KeyboardInterrupt:
        changeFlightMode2('MANUAL')
        drone.mav.command_long_send(
            drone.target_system,
            drone.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
            0, #Confirmation
            0, #Params (1 - 7)
            0, 0, 0, 0, 0, 0
        )
        exit()
    changeFlightMode2('MANUAL')
    drone.mav.command_long_send(
    drone.target_system,
    drone.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
    0, #Confirmation
    0, #Params (1 - 7)
    0, 0, 0, 0, 0, 0
    )
    exit()


if __name__ == "__main__":
    main()
