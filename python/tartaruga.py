import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import numpy as np
from typing import Iterable

class PararTartaruga(Exception):
    def __init__(self):
        super().__init__("Parando tartaruga...")


class NavegadorTartaruga(Node):

    '''
    Classe responsável por controlar a navegação da tartaruga até um determinado ponto
    '''

    def __init__(self, cords_destino: Iterable[int], velocidade_linear: float):
        super().__init__("movimento_da_tartaruga")
        self.cords_destino = np.array(cords_destino)
        self.velocidade_linear = velocidade_linear
        self.cords_atuais = np.array([5.50,5.50])
        self.theta = 0
        self.virou = False

        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel",5)
        self.subscription = self.create_subscription(Pose, "/turtle1/pose", self.atualizar_infos, 10)
        self.timer = self.create_timer(0.1, self.tomar_decisao)
    
    def atualizar_infos(self, msg: Pose) -> None: 

        '''
        Atualiza as informações atuais da tartaruga

        Args:
            msg(Pose): mensagem recebida pelo tópico pose da tartaruga, contento velocidades lineares, angulares e
            ângulo de direção
        '''
        
        self.cords_atuais = np.array([msg.x,msg.y])
        self.theta = msg.theta
        self.get_logger().info(f"Coords atuais: {self.cords_atuais}, theta: {self.theta}")
    
    def andar(self, velocidade: float, eixo: str) -> None:

        '''
        Faz a tartaruga andar

        Args:   
            velocidade(float): Velocidade(em m/s) com que a tartaruga anda, se velocidade > 0 a tartaruga
                anda para frente, caso velocidade < 0 a tartaruga anda pra trás
            direcao(str): Eixo para pelo qual a tartaruga deve andar
        
        Raises:
            ValueError: Se o eixo fornecido for inválido(diferente de x  e y)
        '''
        msg = Twist()

        if eixo == "x":
            msg.linear.x = velocidade
        elif eixo == "y":
            msg.linear.y = velocidade
        else:
            raise ValueError("Parâmetro de eixo inexistente")

        self.publisher.publish(msg)
        self.get_logger().info(f"Andando para frente com velocidade linear de {velocidade} m/s")

    def tomar_decisao(self):        

        '''
        Função responsável por tomar a decisão da navegação
        '''

        x1,x2 = self.cords_atuais[0], self.cords_destino[0]
        velocidade_linear = self.velocidade_linear
        if abs(x1 - x2) >= 0.1:
            if x1 > x2:
                velocidade_linear = -velocidade_linear
            self.andar(velocidade=velocidade_linear, eixo="x")
            return
        
        y1,y2 = self.cords_atuais[1], self.cords_destino[1]
        velocidade_linear = self.velocidade_linear
        if abs(y1 - y2) > 0.1:
            if y1 > y2:
                velocidade_linear = -velocidade_linear
            self.andar(velocidade=velocidade_linear, eixo="y")
            return

        print("Tartaruga chegou ao seu destino!")
        self.virou = False
        raise PararTartaruga()
        

def main(args=None):
    rclpy.init(args=args)
    
    print("OBS:Cada coordenada do destino deve ser um número entre 0 e 11")
    x_destino = int(input("X do destino: "))
    y_destino = int(input("y do destino: "))
    if x_destino < 0 or x_destino > 11 or y_destino < 0 or y_destino > 11:
        raise ValueError("As cordenadas do destino são inválidas")
    cords_destino = [x_destino, y_destino]
    no = NavegadorTartaruga(cords_destino=cords_destino, velocidade_linear=0.2)

    try:
        rclpy.spin(no)
    except PararTartaruga as e:
        rclpy.shutdown()
        print(e)

if __name__ == "__main__":
    main()
