#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 5/27/2015
@author: iitoku2
'''

import os

class Config(object):
    #Flask config
    TESTING = False
    PORT = 80
    DEBUG = True

    #DB config
    DB_SERVER = os.environ['DB_SERVER']
    DB_USERNAME = os.environ['DB_USERNAME']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_DATABASE = os.environ['DB_DATABASE']
    DB_PORT = int(os.environ['DB_PORT'])
