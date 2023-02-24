import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, AppendEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource

PACKAGE = "urdf_demo"
MODEL = "camera"
WORLD = "empty.world"

def generate_launch_description():
    ld = LaunchDescription()

    gazebo_pkg = get_package_share_directory("gazebo_ros")
    pkg = get_package_share_directory(PACKAGE)


    model_sdf_full_path = os.path.join(pkg, "models", MODEL, "model.sdf")
    

    resources = [
        os.path.join(pkg, "worlds")    
    ]

    resource_env = AppendEnvironmentVariable(name="GAZEBO_RESOURCE_PATH", value=":".join(resources))

    models = [
        os.path.join(pkg, "models")    
    ]

    models_env = AppendEnvironmentVariable(name="GAZEBO_MODELS_PATH", value=":".join(models))

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    gazebo_pkg, 'launch', 'gazebo.launch.py')]),
                    launch_arguments={'verbose': "true", "world": WORLD}.items()
             )


    spawn_entity = Node(
        package="gazebo_ros", 
        executable="spawn_entity.py",
        arguments=[
        '-entity', "world_camera", 
        '-file', model_sdf_full_path,
        '-x', "0",
        '-y', "0",
        '-z', "3"],
        output='screen')

    ld.add_action(models_env)
    ld.add_action(resource_env)
    ld.add_action(gazebo)
    ld.add_action(spawn_entity)

    return ld