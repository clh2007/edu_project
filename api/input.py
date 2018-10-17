#coding:utf-8

from tornado.web import RequestHandler
import json
from util.convert import is_mobile
import logging

from logic import Logic
from logic.school import SchoolLogic
from logic.classlogic import ClassLogic
from logic.teacher import TeacherLogic
from logic.student import StudentLogic
from logic.relative import RelativeLogic

LOG = logging.getLogger(__name__)

class RegistryHandler(RequestHandler):
    def post(self, registry_obj):
        try:
            _op = Logic()
            _infos = dict()
            if registry_obj == "school":
                _infos = self._get_school_argument()
                _op = SchoolLogic()

            if registry_obj == "class":
                _infos = self._get_class_argument()
                _op = ClassLogic()

            if registry_obj == "teacher":
                _infos = self._get_teacher_argument()
                _op = TeacherLogic()

            if registry_obj == "student":
                _infos = self._get_student_argument()
                _op = StudentLogic()

            if registry_obj == "relative":
                _infos = self._get_relative_argument()
                _op = RelativeLogic()

            _ = _op.intput(**_infos)
            if _:
                self.finish(json.dumps({'state': 0, 'message': 'input school info success.'}))
            else:
                self.finish(json.dumps({'state': 10, 'message': 'action error'}))
        except Exception as ex:
            LOG.error("Input %s error:%s"%(registry_obj, ex))
            self.finish(json.dumps({'state': 4, 'message': 'input error'}))

    def _get_school_argument(self):
        name = self.get_argument('name', '')
        cardcode = self.get_argument('cardcode', '')
        describe = self.get_argument('describe', '')
        return {
            "name": name,
            "cardcode": cardcode,
            "describe": describe
        }

    def _get_class_argument(self):
        name = self.get_argument('name', '')
        grade = self.get_argument('grade', '')
        school_code = self.get_argument('school_code', '')
        student_number = int(self.get_argument('study_number', 0))
        return {
            "name": name,
            "grade": grade,
            "school_code": school_code,
            "student_number": student_number
        }

    def _get_teacher_argument(self):
        name = self.get_argument('name', '')
        sex = int(self.get_argument('sex', 0))
        age = int(self.get_argument('age', 0))
        school_code = self.get_argument('school_code', '')
        class_code = self.get_argument('school_code', '')
        phone = self.get_argument('phone', '')
        return {
            "name": name,
            "sex": sex,
            "age": age,
            "school_code": school_code,
            "class_code": class_code,
            "phone": phone
        }

    def _get_student_argument(self):
        name = self.get_argument('name', '')
        sex = int(self.get_argument('sex', 0))
        age = int(self.get_argument('age', 0))
        grade = self.get_argument('grade', '')
        class_code = self.get_argument('class_code', '')
        school_code = self.get_argument('school_code', '')
        status = self.get_argument('status', 'apply')
        relation_number = int(self.get_argument('school_code', 3))
        return {
            "name": name,
            "sex": sex,
            "age": age,
            "grade": grade,
            "class_code": class_code,
            "school_code": school_code,
            "status": status,
            "relation_number": relation_number
        }

    def _get_relative_argument(self):
        name = self.get_argument('name', '')
        sex = int(self.get_argument('sex', 0))
        age = int(self.get_argument('age', 0))
        student_code = self.get_argument('student_code', '')
        relation = self.get_argument('relation', '')
        phone = self.get_argument('phone', '')
        return {
            "name": name,
            "sex": sex,
            "age": age,
            "student_code": student_code,
            "relation": relation,
            "phone": phone
        }