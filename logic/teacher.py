#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import datetime
from util.convert import *
from db import api as db_api
from logic import Logic

class TeacherLogic(Logic):
    def __init__(self):
        super(TeacherLogic, self).__init__()

    def intput(self, name="", sex=0, age=0, school_code="", class_code="", phone=""):
        values = {
            "name": name,
            "sex": sex,
            "age": age,
            "school_code": school_code,
            "class_code": class_code,
            "phone": phone
        }
        teacher_obj = db_api.teacher_create(values)
        return teacher_obj

    def output(self):
        pass

    def infos(self, code="", name="", school_code="", school_name="", class_code="", class_name="", phone="", limit=100, offset=1):
        offset = (offset - 1) * limit if offset > 0 else 0
        filters = dict()
        if code:
            filters.update({"code": code})
        if name:
            filters.update({"name": name})
        if school_code or school_name:
            if school_name:
                _school_list = db_api.school_list(name=school_name)
                if not _school_list:
                    return {"count": 0, "state": 0, "message": "query success", "data": []}
                school_code = _school_list[0].code
            filters.update({"school_code": school_code})

        if class_code or class_name:
            if class_name:
                _class_list = db_api.class_list(name=class_name)
                if not _class_list:
                    return {"count": 0, "state": 0, "message": "query success", "data": []}
                class_code = _class_list[0].code
            filters.update({"class_code": class_code})
        if phone:
            filters.update({"phone": phone})

        teacher_list = db_api.teacher_list(offset=offset, limit=limit, **filters)
        teacher_count = db_api.teacher_count(**filters)
        return {"count": teacher_count, "state": 0, "message": "query success", "data": teacher_list}