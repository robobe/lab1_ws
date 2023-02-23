import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.actions import (IncludeLaunchDescription,
    ExecuteProcess,
    RegisterEventHandler,
    LogInfo)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import (OnExecutionComplete, OnProcessExit,
                                OnProcessIO, OnProcessStart, OnShutdown)

PACKAGE = "urdf_demo"
URDF = "robot.xacro"
CONFIG = "rviz_range.rviz"

def generate_launch_description():
    ld = LaunchDescription()

    gazebo_pkg = get_package_share_directory("gazebo_ros")
    pkg = get_package_share_directory(PACKAGE)


    xacro_file = os.path.join(pkg, "urdf", URDF)
    robot_description = Command(['xacro ', xacro_file])

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
            arguments=['-d' + os.path.join(pkg, 'config', CONFIG)]
        )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "demo", "-topic", "robot_description"],
        output="screen",
    )

    # ros2 topic pub -1 /set_joint_trajectory trajectory_msgs/msg/JointTrajectory  '{header: {frame_id: world}, joint_names: [slider_joint, arm_joint],  points: [  {positions: {0.8,0.6}} ]}'
    run_trajectory = ExecuteProcess(
        cmd=[
            "ros2", "topic", "pub", "-1",
            "/set_joint_trajectory",
            "trajectory_msgs/msg/JointTrajectory",
            "'{header: {frame_id: world}, joint_names: [slider_joint, arm_joint],  points: [  {positions: {0.8,0.6}} ] }'"
        ],
        shell=True
    )

    spawn_complete = RegisterEventHandler(
        OnProcessExit(
            target_action=spawn_entity,
            on_exit=[
                LogInfo(msg='Execute trajectory'),
                run_trajectory
            ]
        )
    )

    marker = Node(
        package='urdf_demo',
        executable='range_marker',
        name='range_marker',
    )
    
    ld.add_action(robot_state_publisher)
    ld.add_action(gazebo)
    ld.add_action(spawn_complete)
    ld.add_action(spawn_entity)
    ld.add_action(rviz_node)
    ld.add_action(marker)
    
    return ld