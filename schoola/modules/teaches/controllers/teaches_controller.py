from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.teaches.models import Teaches


class TeachesController(DatabaseResourceController):

    TITLE = 'Teaches'

    TEMPLATE_DIRECTORY_NAME = 'teaches'

    MODEL_CLASS = Teaches

    PRIMARY_KEYS = [
        'ID',
        'course_id',
        'sec_id',
        'semester',
        'year'
    ]
