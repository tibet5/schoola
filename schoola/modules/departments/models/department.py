import sqlalchemy
from schoola.arch.mvc import Model


class Department(Model):

    __tablename__ = 'departments__departments'

    dept_name = sqlalchemy.Column(
        sqlalchemy.VARCHAR(20),
        primary_key=True
    )

    building = sqlalchemy.Column(
        sqlalchemy.VARCHAR(15)
    )

    budget = sqlalchemy.Column(
        sqlalchemy.NUMERIC(12,2)
    )

