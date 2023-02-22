import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from rclpy.qos import qos_profile_system_default

TOPIC = "/set_joint_trajectory"
PERIOD = 1

class MyNode(Node):
    def __init__(self):
        node_name="simple_trajectory"
        super().__init__(node_name)
        self.pub = self.create_publisher(JointTrajectory, TOPIC, qos_profile_system_default)
        self.timer = self.create_timer(PERIOD, self.__timer_handler)
        self.get_logger().info("Hello ROS2")

    def __timer_handler(self):
        points = JointTrajectoryPoint()
        points.positions.append(0.5)
        points.positions.append(0.5)
        msg = JointTrajectory()
        msg.header.frame_id = "world"
        msg.joint_names.append("slider_joint")
        msg.joint_names.append("arm_joint")
        msg.points.append(points)

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()