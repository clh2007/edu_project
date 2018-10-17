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

class InfosHandler(RequestHandler):
    def get(self, registry_obj):
        limit = int(self.get_argument('limit', 100))
        offset = int(self.get_argument('offset', 1))
        try:
            _op = Logic()
            _value = dict()
            if registry_obj == "school":
                _value = self._get_school_argument()
                _op = SchoolLogic()

            if registry_obj == "class":
                _value = self._get_class_argument()
                _op = ClassLogic()

            _ = _op.infos(limit=limit, offset=offset, **_value)
            if _:
                self.finish(json.dumps(_))
            else:
                self.finish(json.dumps({'state': 10, 'message': 'action error'}))
        except Exception as ex:
            LOG.error("query %s error:%s"%(registry_obj, ex))
            self.finish(json.dumps({"count": 0, "state":1, "message":"error", "data":[]}))


    def _get_school_argument(self):
        code = self.get_argument('code', '')
        name = self.get_argument('name', '')
        cardcode = self.get_argument('cardcode', '')

    def _get_class_argument(self):
        code = self.get_argument('code', '')
        name = self.get_argument('name', '')
        grade = self.get_argument('grade', '')
        school_code = self.get_argument('school_code', '')
        school_name = self.get_argument('school_code', '')

    def _get_teacher_argument(self):
        code = self.get_argument('code', '')
        name = self.get_argument('name', '')
        school_code = self.get_argument('school_code', '')
        school_name = self.get_argument('school_name', '')
        class_code = self.get_argument('school_code', '')
        class_name = self.get_argument('class_name', '')

    def _get_student_argument(self):
        code = self.get_argument('code', '')
        name = self.get_argument('name', '')
        grade = self.get_argument('grade', '')
        school_code = self.get_argument('school_code', '')
        school_name = self.get_argument('school_name', '')
        class_code = self.get_argument('class_code', '')
        class_name = self.get_argument('class_name', '')
        relative_code = self.get_argument('relative_code', '')
        relative_name = self.get_argument('relative_name', '')

    def _get_relative_argument(self):
        code = self.get_argument('code', '')
        name = self.get_argument('name', '')
        student_code = self.get_argument('student_code', '')
        student_name = self.get_argument('student_name', '')
        school_code = self.get_argument('school_code', '')
        school_name = self.get_argument('school_name', '')
        phone = self.get_argument('phone', '')
