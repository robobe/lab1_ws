# lab2
## objective

- Switch to xacro
- Using launch with arguments
  - control xacro from launch file

## to read
- [Getting Ready for ROS Part 7: Describing a robot with URDF](https://articulatedrobotics.xyz/ready-for-ros-7-urdf/)

## Quiz
1. Convert urdf to xacro
   1. use macro, include, property
   2. Add utils.xacro with inerta macro and color definition
2. Write launch file to view xacro in RVIZ
3. Add `argument` to xacro and launch file
   1. argument control base link color
4. `ros2 launch urdf_demo lab2_v2.launch.py base_link_color:=black`
   1. Why red not work
   2. Fix it

## Result
### quiz1
#### 1.1
[main robot xacro](src/urdf_demo/urdf/robot.xacro)
#### 1.2
[utils](src/urdf_demo/urdf/utils.xacro)

### quiz2
[launch](src/urdf_demo/launch/lab2_v1.launch.py)

### quiz3
[launch with argument](src/urdf_demo/launch/lab2_v2.launch.py)

```
ros2 launch urdf_demo lab2_v2.launch.py -s
```

```
ros2 launch urdf_demo lab2_v2.launch.py -s
Arguments (pass arguments as '<name>:=<value>'):

    'base_link_color':
        switch base link color between blue to  white
        (default: 'blue')

```

```
ros2 launch urdf_demo lab2_v2.launch.py base_link_color:=white
```

### quiz4
```xml
<material name="blue">
    <color rgba="0.2 0.2 1 1"/>
</material>
```