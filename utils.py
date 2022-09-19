#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "captaincook-del"
__version__ = "1.0"

# pylint: disable=missing-module-docstring, wrong-import-position, import-error
# pylint: disable=undefined-variable, unused-variable, unused-import

""" Toolkit """
import logging
import binascii
from base64 import b64decode, b64encode
from os import walk, getcwd
from os.path import join, isdir
from logging.handlers import TimedRotatingFileHandler

from yaml import safe_load
from yaml import YAMLError

NAME = 'utils'
REQUIRED_GLOBALS = frozenset(['name'])

""" Color  """
# Reset
OFF='\033[0m'       # Text Reset

# Regular Colors
BLACK='\033[0;30m'        # BLACK
RED='\033[0;31m'          # RED
GREEN='\033[0;32m'        # GREEN
YELLOW='\033[0;33m'       # YELLOW
BLUE='\033[0;34m'         # BLUE
PURPLE='\033[0;35m'       # PURPLE
CYAN='\033[0;36m'         # CYAN
WHITE='\033[0;37m'        # WHITE

# Bold
BBLACK='\033[1;30m'       # BLACK
BRED='\033[1;31m'         # RED
BGREEN='\033[1;32m'       # GREEN
BYELLOW='\033[1;33m'      # YELLOW
BBLUE='\033[1;34m'        # BLUE
BPURPLE='\033[1;35m'      # PURPLE
BCYAN='\033[1;36m'        # CYAN
BWHITE='\033[1;37m'       # WHITE

# Underline
UBLACK='\033[4;30m'       # BLACK
URED='\033[4;31m'         # RED
UGREEN='\033[4;32m'       # GREEN
UYELLOW='\033[4;33m'      # YELLOW
UBLUE='\033[4;34m'        # BLUE
UPURPLE='\033[4;35m'      # PURPLE
UCYAN='\033[4;36m'        # CYAN
UWHITE='\033[4;37m'       # WHITE

# Background
ON_BLACK='\033[40m'       # BLACK
ON_RED='\033[41m'         # RED
ON_GREEN='\033[42m'       # GREEN
ON_YELLOW='\033[43m'      # YELLOW
ON_BLUE='\033[44m'        # BLUE
ON_PURPLE='\033[45m'      # PURPLE
ON_CYAN='\033[46m'        # CYAN
ON_WHITE='\033[47m'       # WHITE

logger_formatter = logging.Formatter(
    '%(asctime)s [%(name)s] : %(levelname)s %(message)s',
    datefmt='%B. %d %H:%M:'
)
c_logger = logging.getLogger(NAME)
handler_logger = logging.handlers.TimedRotatingFileHandler(
    "./"+NAME+".log",
    when="D",
    interval=1,
    encoding="utf-8",
    backupCount=7
)

handler_logger.setFormatter(logger_formatter)
c_logger.addHandler(handler_logger)
c_logger.setLevel(logging.DEBUG)

def load_config(filepath='config.yaml'):
    """ Function wich import parameter """
    try:
        with open(filepath, 'r', encoding='utf8') as stream:
            try:
                conf = safe_load(stream)
            except YAMLError:
                c_logger.exception('Error in reading the file {0}'.format(filepath))
    except FileNotFoundError:
        c_logger.exception('File not found: {0}'.format(filepath))
        return None
    if REQUIRED_GLOBALS-frozenset(list(conf.keys())):
        c_logger.exception('There are missing olbigatory parameters in{0}'.format(filepath))
        raise Exception('There are missing olbigatory parameters in{0}'.format(filepath))

    return conf

def camel_case_2snake_case(camel_case):
    """ Transform CamelCase to snake_case """
    snake_case = ""
    for ind,letter in enumerate(camel_case):
        if letter.isupper() and ind != 0:
            snake_case+="_"
        snake_case+=letter.lower()
    return snake_case

def snake_case_2camel_case(snake_case):
    """ Transform snake_case to CamelCase """
    camel_case = ""
    is_upper = False

    for ind,letter in enumerate(snake_case):
        if not letter.isalpha():
            is_upper = True
        elif is_upper:
            camel_case+= letter.upper()
            is_upper = False
        else:
            camel_case+=letter
    return camel_case

def isb64(data):
    """ Test is the data is in base 64 """
    test = False
    try:
        test = bytes.decode(b64encode(b64decode(data))) == data.decode("utf-8")
    except binascii.Error:
        pass
    return test

def b64dec(data):
    """ Decode the data in base64 """
    return b64decode(data).decode("utf-8")

def encode64(data):
    """ Encode the string data in base64 """
    return b64encode(data.encode('ascii'))

def tree_path(path=getcwd(), add_hidden=False):
    """ construct a tree of the path with all files and subdirectories """
    # if path exist but is empty
    if not path:
        path = getcwd()

    if not isdir(path):
        return ["Path is not a directory"]

    file_list = []
    for root, dirs, files in walk(path):
        for file in files:
            # print(f"file {join(root, file)}")
            if add_hidden or not is_hidden(join(root, file)):
                file_list.append(join(root, file))
    return file_list

def is_hidden(filename):
    """ Check if the file is hidden and return True if it is """
    return any([file for file in filename.split("/") if file.startswith(".") or file.startswith("__")])