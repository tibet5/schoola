import sqlalchemy
from schoola.arch.mvc import Model


class Section(Model):

    __tablename__ = 'sections__sections'

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

    building = sqlalchemy.Column(
        sqlalchemy.VARCHAR(15)
    )

    room_number = sqlalchemy.Column(
        sqlalchemy.VARCHAR(7)
    )

    time_slot_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(4)
    )
