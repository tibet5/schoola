from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.sections.models import Section


class SectionController(DatabaseResourceController):

    TITLE = 'Section'

    TEMPLATE_DIRECTORY_NAME = 'sections'

    MODEL_CLASS = Section

    PRIMARY_KEYS = [
        'course_id',
        'sec_id',
        'semester',
        'year'
    ]
