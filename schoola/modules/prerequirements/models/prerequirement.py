import sqlalchemy
from schoola.arch.mvc import Model


class Prerequirement(Model):

    __tablename__ = 'prereq_prereq'
    course_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(8),
        primary_key=True
    )

    prereq_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(8),
        primary_key=True

    )
