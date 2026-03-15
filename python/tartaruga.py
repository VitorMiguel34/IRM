import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ControlarTartaruga(Node):
    def __init__(self):
        super().__init__("movimento_da_tartaruga")

        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel",5)
        self.timer = self.create_timer(0.5,self.fazer_espiral)
        self.velocidade = 0.0
    
    def fazer_espiral(self):
        self.velocidade += 0.1

        msg = Twist()
        msg.linear.x = self.velocidade
        msg.angular.z = 2.0

        self.publisher.publish(msg)
        self.get_logger().info(f"Velocidade linear: {self.velocidade}")


def main(args=None):
    rclpy.init(args=args)
    no = ControlarTartaruga()
    rclpy.spin(no)

if __name__ == "__main__":
    main()
