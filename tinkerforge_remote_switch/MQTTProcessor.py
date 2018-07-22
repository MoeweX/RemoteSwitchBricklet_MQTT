# coding=utf-8
import logging
import paho.mqtt.client as mqtt

from tinkerforge_remote_switch import CONFIG
from tinkerforge_remote_switch.RSBController import RSBController

LOG = logging.getLogger(__name__)

class MQTTProcessor(object):

    def __init__(self, rsb_controller):
        """

        :type rsb_controller: RSBController
        """
        self.__rsb_controller = rsb_controller

        self.__client = mqtt.Client("RemoteSwitchBricklet", clean_session=False)
        self.__client.connect(CONFIG.broker_address)

        self.__client.on_message = self.__on_message
        self.__client.subscribe(CONFIG.subscribe_prefix + "/#")
        self.__client.loop_start()

        LOG.info("MQTTProcessor running")

    # noinspection PyUnusedLocal
    def __on_message(self, client, userdata, message):
        topic = message.topic
        payload = str(message.payload.decode("utf-8"))
        LOG.debug("Message topic: {0}".format(topic))
        LOG.debug("Message payload: {0}".format(payload))

        topic_array = topic.split("/")
        if len(topic_array) != 4:
            LOG.warning("Topic {0} has more than four parts".format(topic))

        if payload == "0":
            self.__rsb_controller.add_socket_switch_operation_to_queue(topic_array[2], topic_array[3], 0)
        elif payload == "1":
            self.__rsb_controller.add_socket_switch_operation_to_queue(topic_array[2], topic_array[3], 1)
        else:
            LOG.warning("Payload {0} for topic {0} is not valid".format(payload, topic))

    def publish(self, address, unit, state):
        topic = CONFIG.publish_prefix + "/{0}/{1}".format(address, unit)
        self.__client.publish(topic, str(state))
