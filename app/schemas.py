# File: app/schemas.py
from app.models import Trigger, EventLog
from app import ma

class TriggerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trigger

class EventLogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EventLog
