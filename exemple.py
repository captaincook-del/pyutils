#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "captaincook-del"
__version__ = "beta"
__status__ = "Production"

"""
Exemple fo using utils.py
"""

from utils import load_config
from utils import c_logger

if __name__ == "__main__":
    c_logger.info("Exemple start")
    conf = load_config()
    print(conf)
    c_logger.debug(conf)
    c_logger.info("Exemple end")