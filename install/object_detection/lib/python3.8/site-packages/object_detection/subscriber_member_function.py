# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2D
from vision_msgs.msg import ObjectHypothesisWithPose
from vision_msgs.msg import Detection2DArray
from std_srvs.srv import SetBool


class ObjectDetection(Node):

    def __init__(self):
        super().__init__('object_detection')

        self.subscription = self.create_subscription(
            Detection2DArray,
            "detections",
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Center position x: %f' % msg.detections.bbox.center.position.x)


def main(args=None):
    rclpy.init(args=args)

    object_detection_publisher = ObjectDetection()

    rclpy.spin(object_detection_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    object_detection_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
