import sqlalchemy
from schoola.arch.mvc import Model


class Teaches(Model):

    __tablename__ = 'teaches__teaches'

    ID = sqlalchemy.Column(
        sqlalchemy.VARCHAR(5),
        primary_key=True
    )

    course_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(8),
        sqlalchemy.Sequence(
            'course_id_seq'
        ),
        primary_key=True
    )

    sec_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(8),
        primary_key=True
    )


    semester = sqlalchemy.Column(
        sqlalchemy.VARCHAR(6),
        primary_key=True
    )

    year = sqlalchemy.Column(
        sqlalchemy.NUMERIC(4,0),
        primary_key=True
    )

