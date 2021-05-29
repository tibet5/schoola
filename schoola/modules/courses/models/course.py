import sqlalchemy
from schoola.arch.mvc import Model


class Course(Model):

    __tablename__ = 'courses__courses'

    course_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(8),
        primary_key=True
    )

    title = sqlalchemy.Column(
        sqlalchemy.VARCHAR(50)
    )

    dept_name = sqlalchemy.Column(
        sqlalchemy.VARCHAR(20)
    )
    credit = sqlalchemy.Column(
        sqlalchemy.NUMERIC(2,0)
    )

