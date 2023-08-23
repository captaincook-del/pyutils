#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "captaincook-del"
__version__ = "1.O"

""" Exemple fo using utils.py """

from json import dumps

from utils import *
from logger import LOGGER

if __name__ == "__main__":
    LOGGER.set_debug()
    LOGGER.info("Exemple start")

    print(YELLOW + "A little test of color prompt" + OFF)
    conf = load_config()
    print("configuration loaded in yml: ", dumps(conf, indent=4))
    print("HelloWorld to : "+camel_case_2snake_case("HelloWorld"))
    print("hello_world to : "+snake_case_2camel_case("hello_world"))

    print()
    data_b64 = encode64("Hey man")
    print("A string in base64 ", data_b64)
    print("Test if the data is in bas64 :", isb64(data_b64))
    print("The string decoded is : ",b64dec(data_b64))

    print()
    paths = tree_path()
    print("list of current tree path: ", dumps(paths, indent=4))
    LOGGER.debug(conf)
    LOGGER.info("Exemple end")
