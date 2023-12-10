# RoboSub 2023

The source code and documentation for the Lehihg Underwater Robotics Team

### Google Drive
- Includes: Past years files, accound credentials, presentations, etc.
- Email inuwrobo@lehigh.edu to request for access

### Team Wiki: https://docs.lehighur.org
- Includes Tutorials:
  - Mavproxy Setup on Jetson
  - YOLOv8 Setup on Jetson Orin
  - Using FFmpeg to Record Camera
  - Training with YOLOv8
   
### Other Useful Links
- Pixhawk4 Autopilot User Guide: [https://docs.px4.io/](https://docs.px4.io/main/en/)
- Mavlink Documentation: [https://ardupilot.org/dev/docs/mavlink-basics.html](https://ardupilot.org/dev/docs/mavlink-basics.html)
- ArduSub: https://www.ardusub.com/
- ROS2 Foxy: https://docs.ros.org/en/foxy/
- YOLOv8 package for ROS2: [https://github.com/mgonzs13/yol0v8_ros](https://github.com/mgonzs13/yolov8_ros)
- Roboflow with YOLOv8: https://roboflow.com/model/yolov8
- Behavioral Tree Documentation: https://www.behavioraltree.dev/docs/intro/

# ROS2 Source Code

The ROS2 code that has object detection and processing for RoboSub2023 task images.

## Getting Started

Setup environment

1. Create a ROS2 workspace: https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html
2. Navigate to that workspace
3. Clone the repository to the src folder of the workspace
   
Cloning tutorial: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository



### Prerequisites

Make sure the following requirements are downloaded and satisfied:

- Opearting System: Ubuntu 20.04.6 LTS
- ROS2 Foxy
  - Installation: https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html
- Intelrealsense ROS2 package
  - Installation: https://github.com/IntelRealSense/realsense-ros    



## Running the code

### Launching the intel real sense node

To launch the intelrealsense node navigate to the directory where you stored it and run:

```
~$ ros2 run realsense2_camera realsense2_camera_node
```

### Launching the ROS2 YOLOv8 node

Open up another terminal and navigate back to your workspace where the source code is store and run:

```
~/ros2_ws$ source ./install/setup.bash
~/ros2_ws$ colcon build ./run
~/ros2_ws$ ros2 launch ./src/yolov8_ros/yolov8_bringup/launch/yolov8.launch.py
```

### Launching the object detection processing node

Open up another terminal and navigate to the src folder of the workspace and run:

```
~/ros2_ws/src$ source ./install/setup.bash
~/ros2_ws/src$ ros2 run object_detection object_detection_sub
```

### Visual testing

To view the bounding boxes of the object detection run "$ rviz2" and select yolov8/detections topic.

To view a visual representation off the nodes' communication run "$ rqt_grap" while in the root of the ROS2 workspace.

