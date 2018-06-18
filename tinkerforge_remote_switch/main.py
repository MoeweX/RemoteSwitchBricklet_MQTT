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

    tinkerforgeSender.addSocketSwitchOperationToQueue(29, 2, 1)
    tinkerforgeSender.addSocketSwitchOperationToQueue(30, 3, 1)
    tinkerforgeSender.addSocketSwitchOperationToQueue(29, 1, 1)
    tinkerforgeSender.addSocketSwitchOperationToQueue(31, 2, 1)

    time.sleep(3)

    tinkerforgeSender.addSocketSwitchOperationToQueue(30, 3, 0)
    tinkerforgeSender.addSocketSwitchOperationToQueue(29, 1, 0)
    tinkerforgeSender.addSocketSwitchOperationToQueue(31, 2, 0)

    # wait for user input to shut down application
    raw_input()
    tinkerforgeSender.shutdown()
