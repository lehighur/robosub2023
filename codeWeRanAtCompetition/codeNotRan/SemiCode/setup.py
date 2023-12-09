from pymavlink import mavutil
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
