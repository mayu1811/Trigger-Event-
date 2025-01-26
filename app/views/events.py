# File: app/views/events.py
from flask import Blueprint, jsonify
from app.models import EventLog
from app.schemas import EventLogSchema

event_blueprint = Blueprint('events', __name__, url_prefix='/events')

@event_blueprint.route('/', methods=['GET'])
def get_events():
    events = EventLog.query.all()
    return EventLogSchema(many=True).jsonify(events), 200
