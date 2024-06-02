#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7426935110:AAH7rYc_pnh72lznF5rOC5q9EjL_Lxd9Bgk")
    API_ID = int(os.environ.get("API_ID", "21311076"))
    API_HASH = os.environ.get("API_HASH", "7e542efdc73d08a4b382b5d6754c072d")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1782965867")
