# lab4
## Objective

- Add Sensors
  - camera
  - imu
  - range
- capture camera topic using cv_bridge 
- more launch features
 
## Exercise
1. Add sensors
   1. camera sensor
      1. Explain `camera_link_optical` role
   2. range sensor
      1. mount sensor opposite to the camera
   3. imu
      1. mount sensor with the range sensor
2. Write simple node viewer 
3. Run rviz after gazebo launched , using Timer or other method


## Tips
- Don't forget to add optical link frame to fix camera coordinate frame [...]()

## To read
- [Learn about event handlers in ROS 2 launch files](https://docs.ros.org/en/foxy/Tutorials/Intermediate/Launch/Using-Event-Handlers.html#event-handlers-example-launch-file)
## Result

![](images/camera_tf_rviz_camera_coordinate.png)
1. [check gazebo.xacro for sensor](src/urdf_demo/urdf/gazebo.xacro)
2. [simple viewer](src/urdf_demo/urdf_demo/simple_image_viewer.py)
3. [rviz with timer action ](src/urdf_demo/launch/lab4_v2.launch.py)