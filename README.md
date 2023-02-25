# lab6
## Objective
- move to ros control

!!! tip "disabled"
      gazebo plugin for joint state and trajectory
     

## To read
- [Making a Mobile Robot #12 - ros2_control Concept & Simulation](https://articulatedrobotics.xyz/mobile-robot-12-ros2-control/)
- [gazebo_ros2_control](https://github.com/ros-controls/gazebo_ros2_control)
## Exercise
1. Convert URDF to support ros2_control
   1. use position control for both joints
2. Write basic launch file to launch gazebo and rviz
   1. launch (what missing)
3. Run control command from cli for `joint state publisher`
4. Extend the launch file control joint with position controller
   1. change slider and arm joint position from cli
5. Change the slider joint to `effort` controller
6. support xacro to switch between ros_control and gazebo plugin from launch/xacro argument

## Result

### quiz 1
[add control xacro file](src/urdf_demo/urdf/ros_control.urdf.xacro)
### quiz 2
[launch rviz and gazebo](src/urdf_demo/launch/lab4_v1.launch.py)
### quiz 3
`ros2 run controller_manager spawner joint_state_broadcaster`

### quiz 4
```bash title="pub position command
ros2 topic pub --once /position_controller/commands  std_msgs/msg/Float64MultiArray "{data: [10, 1.0]}"
```

### quiz 5
```bash
ros2 topic pub --once /effort_controller/commands  std_msgs/msg/Float64MultiArray "{data: [10]}"
```
