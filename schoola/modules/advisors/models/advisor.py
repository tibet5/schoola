import sqlalchemy
from schoola.arch.mvc import Model


class Advisor(Model):

    __tablename__ = 'advisors__advisors'
    s_ID = sqlalchemy.Column(
        sqlalchemy.VARCHAR(5),
        primary_key=True,
    )

    i_ID = sqlalchemy.Column(
        sqlalchemy.VARCHAR(5),
    )
