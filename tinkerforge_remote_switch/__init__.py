# coding=utf-8

from logging.config import dictConfig
import toml

# enable logging
dictionary = toml.load("../resources/config.toml")
dictConfig(dictionary)
