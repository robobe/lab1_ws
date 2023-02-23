import rclpy
import sys
from rclpy.node import Node
from sensor_msgs.msg import Image
from rclpy.qos import qos_profile_sensor_data
from rclpy.executors import ExternalShutdownException
from cv_bridge import CvBridge
import cv2

TOPIC = "/my_camera/image_raw"

class MyNode(Node):
    def __init__(self):
        node_name="simple_viewer"
        super().__init__(node_name)
        self.__bridge = CvBridge()
        self.create_subscription(Image, TOPIC, self.__image_handler, qos_profile=qos_profile_sensor_data)
        
    def __image_handler(self, msg: Image):
        frame = self.__bridge.imgmsg_to_cv2(msg)
        cv2.imshow("viewer", frame)
        cv2.waitKey(1)

    def dispose(self):
        """
        custom dispose free other node resource
        """
        try:
            cv2.destroyAllWindows()
            print("clear user node resource")
        except:
            print("failed to dispose")
        
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        #todo: self.context.on_shutdown() not working why ??
        node.dispose()
        rclpy.try_shutdown()
        node.destroy_node()
        

if __name__ == '__main__':
    main()