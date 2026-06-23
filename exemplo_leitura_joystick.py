#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy


class JoySubscriber(Node):

    def __init__(self):
        super().__init__('joy_subscriber')

        self.subscription = self.create_subscription(
            Joy,            # Tipo da mensagem
            '/joy',         # Nome do tópico
            self.joy_callback,
            10              # Tamanho da fila
        )

        self.get_logger().info('Aguardando mensagens no tópico /joy...')

    def joy_callback(self, msg):
        # Informações do cabeçalho
        sec = msg.header.stamp.sec
        nanosec = msg.header.stamp.nanosec
        frame_id = msg.header.frame_id

        self.get_logger().info(
            f'Timestamp: {sec}.{nanosec}'
        )

        self.get_logger().info(
            f'Frame ID: {frame_id}'
        )

        # Eixos do joystick
        self.get_logger().info(
            f'Axes ({len(msg.axes)}): {list(msg.axes)}'
        )

        # Botões do joystick
        self.get_logger().info(
            f'Buttons ({len(msg.buttons)}): {list(msg.buttons)}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = JoySubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
