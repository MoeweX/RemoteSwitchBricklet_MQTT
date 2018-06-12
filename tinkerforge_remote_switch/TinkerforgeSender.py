import logging


class TinkerforgeSender(object):
    def __init__(self):
        self.logger = logging.getLogger('TinkerforgeSender')
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug("Initialized TinkerforgeSender.")
