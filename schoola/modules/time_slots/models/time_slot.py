import sqlalchemy
from schoola.arch.mvc import Model


class TimeSlot(Model):

    __tablename__ = 'time_slots_time_slots'
    time_slot_id = sqlalchemy.Column(
        sqlalchemy.VARCHAR(4),
        primary_key=True,
        
    )

    day = sqlalchemy.Column(
        sqlalchemy.VARCHAR(1),
        primary_key=True,
        
    )

    start_hr = sqlalchemy.Column(
        sqlalchemy.Numeric(2),
        primary_key=True,
 
        
    )

    start_min = sqlalchemy.Column(
        sqlalchemy.Numeric(2),
        primary_key=True,
    )

    end_hr = sqlalchemy.Column(
        sqlalchemy.Numeric(2),     

    )

    end_min = sqlalchemy.Column(
        sqlalchemy.Numeric(2), 
    )

