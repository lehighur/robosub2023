import rclpy
from rclpy.node import Node  
import time

from albatross_interfaces.msg import Leak

#leak_message_data 

class subscriber(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            Leak,
            'leak_sensor',
            self.listener_callback,
            5)
        self.subscription
    
    def listener_callback(self, msg):
        self.get_logger().info('recieved "%d"' % msg.leak)
        global leak_message_data
        leak_message_data = str(msg.leak) + "time: " + str(time.time())
    
def main(args = None):
    global leak_message_data
    rclpy.init(args=args)

    sub = subscriber()

    rclpy.spin_once(sub)
    print("Message Recieved A: %s" % leak_message_data)
    print(time.time())
    time.sleep(5)
    print("Message Recieved B: %s" %leak_message_data)
    print(time.time())

if __name__ == '__main__':
    main()