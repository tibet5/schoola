import sqlalchemy
from schoola.arch.mvc import Model


class Classroom(Model):

    __tablename__ = 'classrooms__classrooms'

    room_number = sqlalchemy.Column(
        sqlalchemy.VARCHAR(7),
        sqlalchemy.Sequence(
            'room_number_id_seq',
        ),
        primary_key=True,
    )

    building = sqlalchemy.Column(
        sqlalchemy.VARCHAR(15),
        primary_key=True,
    )

    capacity = sqlalchemy.Column(
        sqlalchemy.NUMERIC(4,0)
    )
