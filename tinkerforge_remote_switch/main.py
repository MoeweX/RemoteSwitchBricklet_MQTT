import time

from tinkerforge_remote_switch.MQTTProcessor import MQTTProcessor
from tinkerforge_remote_switch.TinkerforgeSender import TinkerforgeSender
import logging

if __name__ == '__main__':
    # enable logging
    logging.basicConfig()

    # create objects
    tinkerforge_sender = TinkerforgeSender()
    mqtt_processor = MQTTProcessor(tinkerforge_sender)

    tinkerforge_sender.add_socket_switch_operation_to_queue(29, 2, 1)
    tinkerforge_sender.add_socket_switch_operation_to_queue(30, 3, 1)
    tinkerforge_sender.add_socket_switch_operation_to_queue(29, 1, 1)
    tinkerforge_sender.add_socket_switch_operation_to_queue(31, 2, 1)

    time.sleep(3)

    tinkerforge_sender.add_socket_switch_operation_to_queue(30, 3, 0)
    tinkerforge_sender.add_socket_switch_operation_to_queue(29, 1, 0)
    tinkerforge_sender.add_socket_switch_operation_to_queue(31, 2, 0)

    # wait for user input to shut down application
    raw_input()
    tinkerforge_sender.shutdown()
