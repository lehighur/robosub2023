"""
Example code of how to read and write vehicle parameters using pymavlink
"""

import time
# Import mavutil
from pymavlink import mavutil



# Create the connection
# Need to provide the serial port and baudrate
master = mavutil.mavlink_connection("/dev/ttyACM0", baud=115200)

# Restart the ArduSub board !
master.reboot_autopilot()

# Create the connection
# master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()


# Request parameter
master.mav.param_request_read_send(
    master.target_system, master.target_component,
    b'SCALED_PRESSURE2',
    -1
)

# Print old parameter value
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'].decode("utf-8"), message['param_value']))

time.sleep(1)