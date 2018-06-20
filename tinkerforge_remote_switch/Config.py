# coding=utf-8
import toml


class Config(object):

    def __init__(self, config_file_name):
        dictionary = toml.load(config_file_name)

        tinkerforge = Config.getValueOrDefault(dictionary, "tinkerforge")
        self.host = Config.getValueOrDefault(tinkerforge, "host")
        self.port = Config.getValueOrDefault(tinkerforge, "port")
        self.uid = Config.getValueOrDefault(tinkerforge, "uid")

        mqtt = Config.getValueOrDefault(dictionary, "mqtt")
        self.broker_address = Config.getValueOrDefault(mqtt, "broker_address")
        self.publish_prefix = Config.getValueOrDefault(mqtt, "publish_prefix")
        self.subscribe_prefix = Config.getValueOrDefault(mqtt, "subscribe_prefix")

    @staticmethod
    def getValueOrDefault(dictionary, field):
        try:
            return dictionary[field]
        except KeyError:
            return None
