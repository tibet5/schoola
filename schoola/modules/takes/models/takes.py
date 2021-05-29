import sqlalchemy
from schoola.arch.mvc import Model


class Takes(Model):

    __tablename__ = 'takes_takes'
    ID = sqlalchemy.Column(
        sqlalchemy.VARCHAR(5),
        primary_key=True
    )

    course_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(8),
        primary_key=True
    )

    sec_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(8),
        primary_key=True,
    )

    semester = sqlalchemy.Column(
        sqlalchemy.VARCHAR(6),
        primary_key=True,
    )

    year = sqlalchemy.Column(
        sqlalchemy.Numeric(4,0),
        primary_key=True,
    )

    grade = sqlalchemy.Column(
        sqlalchemy.VARCHAR(2),
    )
