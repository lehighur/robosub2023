import rclpy
from rclpy.node import Node  

from albatross_interfaces.msg import Leak

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
    
def main(args = None):
    rclpy.init(args=args)

    sub = subscriber()

    rclpy.spin(sub)

if __name__ == '__main__':
    main()