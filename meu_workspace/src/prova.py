import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import typer

class TortugaController(Node): # Inspirei na minha ponderada de turtlesim
    def __init__(self):
        super().__init__('tortuga_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        
    def move_forward(self):
        mover = Twist()
        mover.linear.x = 2.0
        self.publisher_.publish(mover)

def main(args=None):
    rclpy.init(args=args)
    tortuga_controller = TortugaController()
    tortuga_controller.move_forward()
    rclpy.spin(tortuga_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# Inspirei na CLI do meu projeto
app = typer.Typer()
@app.command()
def control():
    rclpy.init()
    node = TortugaController()
    print("Controlando")
    while True:
        command = typer.prompt("Selecione uma ação: [Frente, Trás, Esquerda, Direita, Parar, Sair]")
        if command == 'Sair':
            break
        elif command == 'Frente':
            node.send_cmd_vel(0.2, 0.0)
        elif command == 'Trás':
            node.send_cmd_vel(-0.2, 0.0)
        elif command == 'Esquerda':
            node.send_cmd_vel(0.0, 0.5)
        elif command == 'Direita':
            node.send_cmd_vel(0.0, -0.5)
        elif command == 'Parar':
            node.send_cmd_vel(0.0, 0.0)
    rclpy.shutdown()

if __name__ == "__main__":
    app()
