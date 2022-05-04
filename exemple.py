#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "captaincook-del"
__version__ = "1.O"
__status__ = "Production"

""" Exemple fo using utils.py """

from utils import *

if __name__ == "__main__":
    c_logger.info("Exemple start")
    print(YELLOW + "A little test of color prompt" + OFF)
    conf = load_config()
    print(conf)
    print("HelloWorld to : "+camel_case_2snake_case("HelloWorld"))
    print("hello_world to : "+snake_case_2camel_case("hello_world"))

    data_b64 = encode64("Hey man")
    print("A string in base64 ", data_b64)
    print("Test if the data is in bas64 :", isb64(data_b64))
    print("The string decoded is : ",b64dec(data_b64))
    c_logger.debug(conf)
    c_logger.info("Exemple end")
