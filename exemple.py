#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "captaincook-del"
__version__ = "beta"
__status__ = "Production"

"""
Exemple fo using utils.py
"""

from utils import *

if __name__ == "__main__":
    c_logger.info("Exemple start")
    conf = load_config()
    print(conf)
    print("HelloWorld to : "+camel_case_2snake_case("HelloWorld"))
    print("hello_world to : "+snake_case_2camel_case("hello_world"))
    c_logger.debug(conf)
    c_logger.info("Exemple end")