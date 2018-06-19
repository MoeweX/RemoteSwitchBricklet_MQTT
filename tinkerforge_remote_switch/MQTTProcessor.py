# coding=utf-8
import logging
import paho.mqtt.client as mqtt

from tinkerforge_remote_switch.RSBController import RSBController

MQTT_BROKER_ADDRESS = "ubuntuMini.local"


class MQTTProcessor(object):

    def __init__(self, rsb_controller):
        """

        :type rsb_controller: RSBController
        """
        self.__logger = logging.getLogger('MQTTProcessor')
        self.__logger.setLevel(logging.DEBUG)

        self.__rsb_controller = rsb_controller

        self.__client = mqtt.Client("RemoteSwitchBricklet", clean_session=False)
        self.__client.connect(MQTT_BROKER_ADDRESS)

        self.__client.on_message = self.__on_message
        self.__client.subscribe("rsb/in/#")
        self.__client.loop_start()

        self.__logger.info("MQTTProcessor running")

    # noinspection PyUnusedLocal
    def __on_message(self, client, userdata, message):
        topic = message.topic
        payload = str(message.payload.decode("utf-8"))
        self.__logger.debug("Message topic: {0}".format(topic))
        self.__logger.debug("Message payload: {0}".format(payload))

        topic_array = topic.split("/")
        if len(topic_array) != 4:
            self.__logger.warning("Topic {0} has more than four parts".format(topic))

        if payload == "0":
            self.__rsb_controller.add_socket_switch_operation_to_queue(topic_array[2], topic_array[3], 0)
        elif payload == "1":
            self.__rsb_controller.add_socket_switch_operation_to_queue(topic_array[2], topic_array[3], 1)
        else:
            self.__logger.warning("Payload {0} for topic {0} is not valid".format(payload, topic))
