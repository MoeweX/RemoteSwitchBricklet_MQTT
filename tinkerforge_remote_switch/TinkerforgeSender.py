# coding=utf-8
import logging
import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_remote_switch import BrickletRemoteSwitch
from collections import deque
from threading import Thread

HOST = "homebridge.local"
PORT = 4223
UID = "nXN"


class TinkerforgeSender(object):

    def __init__(self):
        self.__logger = logging.getLogger("TinkerforgeSender")
        self.__logger.setLevel(logging.DEBUG)

        self.__ipcon = IPConnection()  # Create IP connection
        self.__rs = BrickletRemoteSwitch(UID, self.__ipcon)  # Create device object
        self.__ipcon.connect(HOST, PORT)  # Connect to brickd

        self.__operations = deque()
        self.__operations_worker = Thread(target=self.__work_operations)
        self.__keep_worker_running = True
        self.__operations_worker.start()

        self.__logger.info("TinkerforgeSender running")

    def add_socket_switch_operation_to_queue(self, address, unit, state):
        """
        Add a switch operation for the given socket to the TinkerforgeSender.

        :param address: the address of the socket
        :param unit: the unit of the socket
        :param state: 0 (off) or 1 (on)
        """
        self.__operations.append([address, unit, state])

    def shutdown(self):
        self.__logger.info("TinkerforgeSender stopping")
        self.__keep_worker_running = False
        while self.__operations_worker.isAlive():
            self.__logger.debug("Waiting for operations worker to stop")
            time.sleep(1)
        self.__ipcon.disconnect()
        self.__logger.info("TinkerforgeSender shutdown")

    def __work_operations(self):
        self.__logger.info("Operations worker running")
        while self.__keep_worker_running:
            if self.__operation_open():
                operation = self.__dequeueOperation()
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
        if state == 0:
            self.__logger.debug("Switching {0}-{1} to off".format(address, unit))
        elif state == 1:
            self.__logger.debug("Switching {0}-{1} to on".format(address, unit))
        else:
            self.__logger.warn("State {0} is no valid switching value".format(state))

        tries = 0
        while self.__rs.get_switching_state() == 1 and tries < 100:
            # wait until ready to switch
            time.sleep(0.01)
            tries += 1

        if tries == 100:
            self.__logger.warn("Sender was not ready to switch again after 100 tries")
            return

        self.__rs.switch_socket_b(address, unit, state)
