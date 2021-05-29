from schoola.arch.mvc import DatabaseResourceController
from schoola.modules.time_slots.models import TimeSlot


class TimeSlotController(DatabaseResourceController):

    TITLE = 'Time Slot'

    TEMPLATE_DIRECTORY_NAME = 'time_slots'

    MODEL_CLASS = TimeSlot

    PRIMARY_KEYS = [
        'time_slot_id',
        'day',
    ]
