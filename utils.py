#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "captaincook-del"
__version__ = "beta"
__status__ = "Production"

# pylint: disable=missing-module-docstring, wrong-import-position, import-error
# pylint: disable=undefined-variable, unused-variable, unused-import

"""
Toolkit
"""
import logging
from logging.handlers import TimedRotatingFileHandler
from yaml import safe_load
from yaml import YAMLError

NAME = 'utils'
REQUIRED_GLOBALS = frozenset(['name'])

logger_formatter = logging.Formatter(
    '%(asctime)s [%(name)s] : %(levelname)s %(message)s',
    datefmt='%B. %d %H:%M:%S'
)
c_logger = logging.getLogger(NAME)
handler_logger = handler_debug = logging.handlers.TimedRotatingFileHandler(
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
    """
    Function wich import parameter
    """
    try:
        with open(filepath, 'r', encoding='utf8') as stream:
            try:
                conf = safe_load(stream)
            except YAMLError:
                age_of_logger.exception('Erreur dans la lecture du fichier %s',filepath)
    except FileNotFoundError:
        age_of_logger.exception('Le fichier %s est introuvable',filepath)
        return None
    if REQUIRED_GLOBALS-frozenset(list(conf.keys())):
        print("ERREUR : impossible de trouver le fichier %s", filepath)
        raise Exception('Il manque des paramètres olbigatoire dans %s', filepath)
        age_of_logger.exception('Il manque des paramètres olbigatoire dans %s', filepath)
    return conf

def camel_case_2snake_case(camel_case):
    """
    Transform CamelCase to snake_case
    """
    snake_case = ""
    for ind,letter in enumerate(camel_case):
        if letter.isupper() and ind != 0:
            snake_case+="_"
        snake_case+=letter.lower()
    return snake_case

def snake_case_2camel_case(snake_case):
    """
    Transform snake_case to CamelCase
    """
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
