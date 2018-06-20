# coding=utf-8
import logging
import time

from tinkerforge_remote_switch import CONFIG

from tinkerforge.ip_connection import IPConnection
from tinkerforge.ip_connection import Error
from tinkerforge.bricklet_remote_switch import BrickletRemoteSwitch
from collections import deque
from threading import Thread

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


class RSBController(object):

    def __init__(self):
        self.__ipcon = IPConnection()  # Create IP connection
        self.__rs = BrickletRemoteSwitch(CONFIG.uid, self.__ipcon)  # Create device object
        self.__ipcon.connect(CONFIG.host, CONFIG.port)  # Connect to brickd

        self.__operations = deque()
        self.__operations_worker = Thread(target=self.__work_operations)
        self.__keep_worker_running = True
        self.__operations_worker.start()

        self.__mqtt = None

        LOG.info("RSBController running")

    # noinspection PyAttributeOutsideInit
    def inject_mqtt_processor(self, mqtt):
        """
        Add an mqtt processor that may be used for message publishing.

        :param mqtt: the mqtt processor
        """
        self.__mqtt = mqtt

    def add_socket_switch_operation_to_queue(self, address, unit, state):
        """
        Add a switch operation for the given socket to the RSBController.

        :param address: the address of the socket
        :param unit: the unit of the socket
        :param state: 0 (off) or 1 (on)
        """
        self.__operations.append([int(address), int(unit), int(state)])

    def shutdown(self):
        LOG.info("RSBController stopping")
        self.__keep_worker_running = False
        while self.__operations_worker.isAlive():
            LOG.debug("Waiting for operations worker to stop")
            time.sleep(1)
        self.__ipcon.disconnect()
        LOG.info("RSBController shutdown")

    def __work_operations(self):
        LOG.info("Operations worker running")
        while self.__keep_worker_running:
            if self.__operation_open():
                operation = self.__dequeueOperation()
                # valid assumptions, as operations can only be added through 'RSBController.add_socket_switch_operation_to_queue'
                self.__switch_socket_B(operation[0], operation[1], operation[2])

            time.sleep(0.01)

    def __operation_open(self):
        if self.__operations:
            return True
        return False

    def __dequeueOperation(self):
        return self.__operations.popleft()

    def __switch_socket_B(self, address, unit, state):
        """
        Switch socket of type B

        :param address: the address of the socket
        :param unit: the unit of the socket
        :param state: 0 (off) or 1 (on)
        """

        try:
            if state == 0:
                LOG.debug("Switching {0}-{1} to off".format(address, unit))
            elif state == 1:
                LOG.debug("Switching {0}-{1} to on".format(address, unit))
            else:
                LOG.warning("State {0} is no valid switching value".format(state))

            tries = 0
            while self.__rs.get_switching_state() == 1 and tries < 100:
                # wait until ready to switch
                time.sleep(0.01)
                tries += 1

            if tries == 100:
                LOG.warning("Sender was not ready to switch again after 100 tries")
                return

            self.__rs.switch_socket_b(address, unit, state)
            self.__mqtt.publish(address, unit, state)
        except Error as err:
            LOG.error(err.description)
