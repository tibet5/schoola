from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.takes.models import Takes


class TakesController(DatabaseResourceController):

    TITLE = 'Takes'

    TEMPLATE_DIRECTORY_NAME = 'takes'

    MODEL_CLASS = Takes

    PRIMARY_KEYS = [
        'ID',
        'course_id',
        'sec_id',
        'semester',
        'year'
    ]
