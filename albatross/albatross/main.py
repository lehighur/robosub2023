"""
Example of how to send MANUAL_CONTROL messages to the autopilot using
pymavlink.
This message is able to fully replace the joystick inputs.
"""

# Import mavutil
from pymavlink import mavutil

# Disable "Broad exception" warning
# pylint: disable=W0703

import time
import sys

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

def main():
    print("Hello World!")

def arm_vehicle():
    # Arm
    # master.arducopter_arm() or:
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0)

    # wait until arming confirmed (can manually check with master.motors_armed())
    print("Waiting for the vehicle to arm")
    master.motors_armed_wait()
    print('Armed!')

def disarm_vehicle():
    # Disarm
    # master.arducopter_disarm() or:
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        0, 0, 0, 0, 0, 0, 0)

    # wait until disarming confirmed
    master.motors_disarmed_wait()


# Change Mode function
# Can choose between MANUAL, STABILIZE, DEPTH HOLD
def change_flight_mode(mode):

    # Check if mode is available
    if mode not in master.mode_mapping():
        print('Unknown mode : {}'.format(mode))
        print('Try:', list(master.mode_mapping().keys()))
        sys.exit(1)

    # Get mode ID
    mode_id = master.mode_mapping()[mode]
    # Set new mode
    # master.mav.command_long_send(
    #    master.target_system, master.target_component,
    #    mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
    #    0, mode_id, 0, 0, 0, 0, 0) or:
    # master.set_mode(mode_id) or:
    master.mav.set_mode_send(
        master.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        mode_id)

    while True:
        # Wait for ACK command
        # Would be good to add mechanism to avoid endlessly blocking
        # if the autopilot sends a NACK or never receives the message
        ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
        ack_msg = ack_msg.to_dict()

        # Continue waiting if the acknowledged command is not `set_mode`
        if ack_msg['command'] != mavutil.mavlink.MAV_CMD_DO_SET_MODE:
            continue

        # Print the ACK result !
        print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
        break

# Go forward
def forward(duration):
    master.mav.manual_control_send(
    master.target_system,
    500,
    0,
    500,
    0,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

# Go Backward
def backward(duration):
    master.mav.manual_control_send(
    master.target_system,
    -500,
    0,
    500,
    0,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

# Go Rightward
def rightward(duration):
    master.mav.manual_control_send(
    master.target_system,
    0,
    500,
    500,
    0,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

# Go leftward
def leftward(duration):
    master.mav.manual_control_send(
    master.target_system,
    0,
    -500,
    500,
    0,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

# Go Upward
def upward(duration):
    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    750,
    0,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

# Go Downward
def downward(duration):
    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    250,
    0,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

# Rotate to the right slowly
def rotate_right(duration):
    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    100,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

# Rotate to the right slowly
def rotate_left(duration):
    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    100,
    0)

    time.sleep(duration)

    master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500,
    0,
    0)

if __name__ == '__main__':
    main()