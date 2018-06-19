# coding=utf-8
import time

from tinkerforge_remote_switch.MQTTProcessor import MQTTProcessor
from tinkerforge_remote_switch.RSBController import RSBController
import logging

if __name__ == '__main__':
    # enable logging
    logging.basicConfig()

    # create objects
    tinkerforge_sender = RSBController()
    mqtt_processor = MQTTProcessor(tinkerforge_sender)

    # inject dependency
    tinkerforge_sender.inject_mqtt_processor(mqtt_processor)

    # tinkerforge_sender.add_socket_switch_operation_to_queue(29, 2, 1)
    # tinkerforge_sender.add_socket_switch_operation_to_queue(30, 3, 1)
    # tinkerforge_sender.add_socket_switch_operation_to_queue(29, 1, 1)
    # tinkerforge_sender.add_socket_switch_operation_to_queue(31, 2, 1)
    #
    # time.sleep(3)
    #
    # tinkerforge_sender.add_socket_switch_operation_to_queue(30, 3, 0)
    # tinkerforge_sender.add_socket_switch_operation_to_queue(29, 1, 0)
    # tinkerforge_sender.add_socket_switch_operation_to_queue(31, 2, 0)



    # wait for user input to shut down application
    input()
    tinkerforge_sender.shutdown()
