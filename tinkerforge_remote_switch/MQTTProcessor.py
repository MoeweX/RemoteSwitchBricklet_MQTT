# coding=utf-8
import logging


class MQTTProcessor(object):
    def __init__(self, tinkerforge_sender):
        self.logger = logging.getLogger('MQTTProcessor')
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("Initialized MQTTProcessor")
        self.tinkerforgeSender = tinkerforge_sender
