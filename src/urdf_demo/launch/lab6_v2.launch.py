import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import (IncludeLaunchDescription,
    RegisterEventHandler,
    DeclareLaunchArgument)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import OnProcessStart

PACKAGE = "urdf_demo"
URDF = "robot.xacro"

def generate_launch_description():
    ld = LaunchDescription()

    gazebo_pkg = get_package_share_directory("gazebo_ros")
    pkg = get_package_share_directory(PACKAGE)

    use_effort = LaunchConfiguration('use_effort')
    use_effort_arg =  DeclareLaunchArgument(
            'use_effort',
            default_value='true',
            description='Use ros2_control if true')

    xacro_file = os.path.join(pkg, "urdf", URDF)
    robot_description = Command(['xacro ', xacro_file, ' use_effort:=', use_effort])

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {
                'use_sim_time': True,
                'robot_description': robot_description
            }
        ]
    )

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    gazebo_pkg, 'launch', 'gazebo.launch.py')]),
                    launch_arguments={'verbose': "true"}.items()
             )

    rviz_node = Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments=['-d' + os.path.join(pkg, 'config', 'rviz.rviz')]
        )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "demo", "-topic", "robot_description"],
        output="screen",
    )

    controller_params_file = os.path.join(pkg,'config','position_and_effort.yaml')

    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[{'robot_description': robot_description},
                    controller_params_file]
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
    )

    pos_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["position_controller"],
    )

    effort_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["effort_controller"],
    )

    delayed_controllers_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[joint_broad_spawner, pos_controller_spawner, effort_controller_spawner],
        )
    )

    
    ld.add_action(use_effort_arg)
    ld.add_action(robot_state_publisher)
    ld.add_action(gazebo)
    ld.add_action(spawn_entity)
    ld.add_action(rviz_node)
    ld.add_action(controller_manager)
    ld.add_action(delayed_controllers_spawner)
    return ld