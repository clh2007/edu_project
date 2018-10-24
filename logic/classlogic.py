#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import datetime
from util.convert import *
from db import api as db_api
from logic import Logic

class ClassLogic(Logic):
    def __init__(self):
        pass

    def intput(self, name="", grade="", school_id="", student_number=0):
        values = {
            "name": name,
            "grade": grade,
            "school_id": school_id,
            "student_number": student_number
        }
        class_obj = db_api.class_create(values)
        return class_obj

    def update(self, id="", **kwargs):
        if not id or not kwargs:
            return False
        _ = db_api.class_update(id, kwargs)
        return _

    def infos(self, id="", name="", school_id="", school_name="", grade="", limit=100, offset=1):
        offset = (offset - 1) * limit if offset > 0 else 0
        filters = dict()
        if id:
            filters.update({"id": id})
        if name:
            filters.update({"name": name})
        if school_id or school_id:
            if school_name:
                _school_list = db_api.school_list(name=school_name)
                if not _school_list:
                    return {"count": 0, "state": 0, "message": "query success", "data": []}
                school_id = _school_list[0].id
            filters.update({"school_id": school_id})

        if grade:
            filters.update({"grade": grade})

        class_list = db_api.class_list(offset=offset, limit=limit, **filters)
        #更新学生数和学校名称
        views_list = self.views(class_list)
        for view in views_list:
            school_list = db_api.school_list(id=view.get("school_id"))
            if school_list:
                view.update({"school_name": school_list[0].name})
            student_count = db_api.student_count(class_id=view.get("id"))
            view.update({"reality_number": student_count})

        class_count = db_api.class_count(**filters)
        return {"count": class_count, "state": 0, "message": "query success", "data": views_list}