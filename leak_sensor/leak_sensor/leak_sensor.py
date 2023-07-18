import RPi.GPIO as GPIO
import rclpy
from rclpy.node import Node
from albatross_interfaces.msg import Leak
import time

#define pins
leak_sensor_input = 13 #Board pin 

class leak_sensor(Node):
    #Pin Setup
    GPIO.setmode(GPIO.BOARD) #pin numbering scheme
    GPIO.setup(leak_sensor_input, GPIO.IN)
    leak = 0
    
    #Node Constructor
    def __init__(self):
        global leak
        #leak = GPIO.input(leak_sensor_input)
        super().__init__('leak_sensor')
        self.publisher_ = self.create_publisher(Leak, 'leak_sensor', 5)
        """msg = LeakSensor
        msg.data = leak"""
        #self.publisher_.publish(msg)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        msg = Leak()
        msg.leak = GPIO.input(leak_sensor_input)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.leak)
        self.i +=1 
        
def main(args=None):
    rclpy.init(args=args)
    
    LeakSensor = leak_sensor()

    rclpy.spin(LeakSensor)

if __name__ == '__main__':
    main()

