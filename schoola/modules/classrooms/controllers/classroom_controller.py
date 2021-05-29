from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.classrooms.models import Classroom


class ClassroomController(DatabaseResourceController):

    TITLE = 'Classroom'

    TEMPLATE_DIRECTORY_NAME = 'classrooms'

    MODEL_CLASS = Classroom

    PRIMARY_KEYS = [
        'room_number',
        'building'
    ]
