#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import datetime
from util.convert import *
from db import api as db_api

class SchoolLogic():
    def __init__(self):
        pass

    def intput(self, name="", cardcode="", describe=""):
        values = {
            "name": name,
            "cardcode": cardcode,
            "describe": describe
        }
        school_obj = db_api.school_create(values)
        return school_obj

    def output(self):
        pass

    def infos(self):
        pass