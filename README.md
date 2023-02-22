# lab3
## Objective

- xacro/urdf gazebo extra tags
  - plugin
- gazebo launch
 
## Exercise
1. Add `gazebo.xacro` file
  - set gazebo color
  - set gazebo join state plugin
2. Write launch file to spawn robot into gazebo and view it in rviz
3. pose_trajectory intro, Pub `/set_joint_trajectory ` from cli, write simple node to pub trajectory 
   1. node has 2 argument one for each joint
  
## Notes
- use `use_sim_time` parameter


## to read
- [Getting Ready for ROS Part 8: Simulating with Gazebo](https://articulatedrobotics.xyz/ready-for-ros-8-gazebo/)

## Quiz
- '/joint_state' topic publish by how?
- joint `<dynamics damping="10.0" friction="10.0"/>` explain


## Result

![](images/lab3_v1.png)

### joint trajectory
```bash
ros2 topic info /set_joint_trajectory 
Type: trajectory_msgs/msg/JointTrajectory
Publisher count: 0
Subscription count: 1

```

```bash
ros2 topic pub -1 /set_joint_trajectory trajectory_msgs/msg/JointTrajectory \
 '{header: {frame_id: world}, \
 joint_names: [slider_joint, arm_joint], \
 points: [  {positions: {0.8,0.6}} ]}'
```
![](images/lab.png)