#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7130569401:AAGx9zEZAt6py6TpD9D83TZh2cHH5G1eYkM")
    API_ID = int(os.environ.get("API_ID", "22923037"))
    API_HASH = os.environ.get("API_HASH", "dfb3666878b3851460a58461c5a50f5b")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6554343173")
