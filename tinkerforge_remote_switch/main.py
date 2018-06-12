import time

from tinkerforge_remote_switch.MQTTProcessor import MQTTProcessor
from tinkerforge_remote_switch.TinkerforgeSender import TinkerforgeSender
import logging

if __name__ == '__main__':
    # enable logging
    logging.basicConfig()

    # create objects
    tinkerforgeSender = TinkerforgeSender()
    mqttProcessor = MQTTProcessor(tinkerforgeSender)

    # wait for user input to shut down application
    time.sleep(1)
    pressed = "peter"
    while str(pressed) != "quit":
        pressed = input("Type quit to quit application: ")
