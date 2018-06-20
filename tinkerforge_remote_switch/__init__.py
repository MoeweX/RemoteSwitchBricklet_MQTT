# coding=utf-8

from logging.config import dictConfig
import toml
from tinkerforge_remote_switch.Config import Config

# enable logging
dictConfig(toml.load("../resources/logging.toml"))

# load configuration
CONFIG = Config("../resources/config.toml")
