from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.students.models import Student


class StudentController(DatabaseResourceController):

    TITLE = 'Student'

    TEMPLATE_DIRECTORY_NAME = 'students'

    MODEL_CLASS = Student

    PRIMARY_KEYS = [
        'ID'
    ]
