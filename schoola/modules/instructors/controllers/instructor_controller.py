from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.instructors.models import Instructor


class InstructorController(DatabaseResourceController):

    TITLE = 'Instructor'

    TEMPLATE_DIRECTORY_NAME = 'instructors'

    MODEL_CLASS = Instructor
