from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.advisors.models import Advisor


class AdvisorController(DatabaseResourceController):

    TITLE = 'Advisor'

    TEMPLATE_DIRECTORY_NAME = 'advisors'

    MODEL_CLASS = Advisor

    PRIMARY_KEYS = [
        's_ID',
        'i_ID',
    ]

