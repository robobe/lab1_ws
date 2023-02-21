import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

PACKAGE = "urdf_demo"

def generate_launch_description():
    ld = LaunchDescription()
    pkg = get_package_share_directory(PACKAGE)
    urdf_path = os.path.join(pkg, "urdf", "robot.urdf")
    with open(urdf_path, "r") as f:
        urdf = f.read()

    
    return ld