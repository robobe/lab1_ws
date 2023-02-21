import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument

PACKAGE = "urdf_demo"
URDF = "robot.xacro"

def generate_launch_description():
    ld = LaunchDescription()
    base_link_color = LaunchConfiguration('base_link_color', default="blue")
    
    base_link_color_arg = DeclareLaunchArgument(
            'base_link_color',
            default_value='blue',
            description='switch base link color between blue to  white')

    pkg = get_package_share_directory(PACKAGE)
    xacro_file = os.path.join(pkg, "urdf", URDF)
    robot_description = Command(['xacro ', xacro_file, ' color:=', base_link_color])

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {
                'robot_description': robot_description
            }
        ]
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher"
    )

    rviz_node = Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments=['-d' + os.path.join(pkg, 'config', 'rviz.rviz')]
        )

    ld.add_action(robot_state_publisher)
    ld.add_action(base_link_color_arg)
    ld.add_action(joint_state_publisher_node)
    ld.add_action(rviz_node)
    return ld