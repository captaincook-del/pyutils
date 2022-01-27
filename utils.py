#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "captaincook-del"
__version__ = "beta"
__status__ = "Production"

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
    Fonction qui permet d'importer les paramètres
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
    # provoque une attribut error si le fichier existe 
    # mais qu'il est vide
    if REQUIRED_GLOBALS-frozenset(list(conf.keys())):
        print("ERREUR : impossible de trouver le fichier %s", filepath)
        raise Exception('Il manque des paramètres olbigatoire dans {}'.format(filepath))
        age_of_logger.exception('Il manque des paramètres olbigatoire dans %s', filepath)
    return conf