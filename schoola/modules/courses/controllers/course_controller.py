from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.courses.models import Course


class CourseController(DatabaseResourceController):

    TITLE = 'Course'

    TEMPLATE_DIRECTORY_NAME = 'courses'

    MODEL_CLASS = Course

    PRIMARY_KEYS = [
        'course_id'
    ]
