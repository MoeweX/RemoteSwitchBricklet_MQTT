import logging

class MQTTProcessor(object):
    def __init__(self, tinkerforgeSender):
        self.logger = logging.getLogger('MQTTProcessor')
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("Initialized MQTTProcessor")
        self.tinkerforgeSender = tinkerforgeSender



