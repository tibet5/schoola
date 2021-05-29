from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.departments.models.department import Department


class DepartmentController(DatabaseResourceController):

    TITLE = 'Department'

    TEMPLATE_DIRECTORY_NAME = 'departments'

    MODEL_CLASS = Department

    PRIMARY_KEYS = [
        'dept_name'
    ]
