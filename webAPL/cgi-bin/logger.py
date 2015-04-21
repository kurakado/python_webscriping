#!/usr/bin/python

import logging

LOG_FILENAME = 'debug.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

def logger(string):
    logging.debug(str(string))
