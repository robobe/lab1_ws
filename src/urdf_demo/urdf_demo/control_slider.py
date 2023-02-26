import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from rclpy.qos import qos_profile_sensor_data
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
TOPIC = "/joint_states"
PERIOD = 1

class MyNode(Node):
    def __init__(self):
        node_name="slider_control"
        super().__init__(node_name)
        self.group = ReentrantCallbackGroup()
        self.__slider_index = None
        self.create_subscription(JointState,
            TOPIC,
            self.__joint_state_handler,
            qos_profile=qos_profile_sensor_data,
            callback_group=self.group)

        
    def __joint_state_handler(self, msg: JointState):
        if self.__slider_index is None:
            for pos, name in enumerate(msg.name):
                if name == "slider_joint":
                    self.__slider_index = pos
                    self.get_logger().info(f"pos: {pos}")


def main(args=None):
    rclpy.init(args=args)
    try:
        node = MyNode()
        executor = MultiThreadedExecutor(num_threads=4)
        executor.add_node(node)
        try:
            executor.spin()
        finally:
            node.destroy_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()