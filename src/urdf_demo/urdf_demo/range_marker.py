import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
from std_msgs.msg import Header, ColorRGBA
from sensor_msgs.msg import Range
from builtin_interfaces.msg import Duration

from rclpy.qos import qos_profile_system_default, qos_profile_sensor_data

TOPIC_MARKER = "/visualization_marker"
TOPIC_RANGE = "/ultrasound/range"

class MyNode(Node):
    def __init__(self):
        node_name="simple_marker"
        super().__init__(node_name)
        self.__marker_publisher = self.create_publisher(Marker, TOPIC_MARKER, qos_profile_system_default)
        self.create_subscription(Range, TOPIC_RANGE, self.__range_handler, qos_profile=qos_profile_sensor_data)
    
    def __range_handler(self, msg: Range):
        self.get_logger().info(f"---{msg.range}")
        range = round(msg.range,2)
        pose = Pose(position=Point(x=0.5, y=0.5, z=1.45), orientation=Quaternion(x=0.0, y=0.0, z=0.0, w=1.0))
        marker = Marker(
                type=Marker.TEXT_VIEW_FACING,
                id=0,
                lifetime=Duration(sec=1),
                pose=pose,
                scale=Vector3(x=0.6, y=0.6, z=0.6),
                header=Header(frame_id='world'),
                color=ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.8),
                text=f"{range}")
        self.__marker_publisher.publish(marker)
        

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()