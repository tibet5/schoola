from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.prerequirements.models.prerequirement import Prerequirement


class PrerequirementController(DatabaseResourceController):

    TITLE = 'Prerequirement'

    TEMPLATE_DIRECTORY_NAME = 'prerequirements'

    MODEL_CLASS = Prerequirement

    PRIMARY_KEYS = [
        'course_id',
        'prereq_id',
    ]
