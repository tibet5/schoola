import sqlalchemy
from schoola.arch.mvc import Model


class Instructor(Model):

    __tablename__ = 'instructors__instructors'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.Sequence(
            'instructor_id_seq',
        ),
        primary_key=True,
    )

    name = sqlalchemy.Column(
        sqlalchemy.String,
    )

    dept_name = sqlalchemy.Column(
        sqlalchemy.String,
    )

    salary = sqlalchemy.Column(
        sqlalchemy.Integer,
    )
