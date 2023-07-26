import os

from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

def generate_launch_description():
    yoloconfig = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('yolov8_bringup'),
                'launch',
                'yolov8.launch.py'
            ])
        ])
    )

    return LaunchDescription([
        Node(
            package='realsense2_camera',
            #namespace = 'camera'
            executable='realsense2_camera_node', 
            #name = 'camera'
        ),
        yoloconfig
    ])
