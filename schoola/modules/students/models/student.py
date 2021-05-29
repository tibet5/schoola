import sqlalchemy
from schoola.arch.mvc import Model


class Student(Model):

    __tablename__ = 'students__students'

    ID = sqlalchemy.Column(
        sqlalchemy.INTEGER,
        sqlalchemy.Sequence(
            'student_id_seq'
        ),
        primary_key=True
    )

    name = sqlalchemy.Column(
        sqlalchemy.VARCHAR(20)
    )

    dept_name = sqlalchemy.Column(
        sqlalchemy.VARCHAR(20)
    )

    tot_cred = sqlalchemy.Column(
        sqlalchemy.Integer
    )
