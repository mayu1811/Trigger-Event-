# File: app/views/triggers.py
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from app import db
from app.models import Trigger
from app.schemas import TriggerSchema
from app.tasks.scheduler import fire_trigger

trigger_blueprint = Blueprint('triggers', __name__, url_prefix='/triggers')

@trigger_blueprint.route('/', methods=['POST'])
def create_trigger():
    """
    Create a new trigger (scheduled or API).
    """
    data = request.json
    trigger_type = data.get('type')
    config = data.get('config', {})

    if trigger_type not in ['scheduled', 'api']:
        return jsonify({"error": "Invalid trigger type"}), 400

    new_trigger = Trigger(name=data['name'], type=trigger_type, config=config)
    db.session.add(new_trigger)
    db.session.commit()

    # If scheduled, set up Celery task
    if trigger_type == 'scheduled':
        schedule = config.get('schedule')  # e.g., {'interval': 30, 'unit': 'minutes'}
        if not schedule:
            return jsonify({"error": "Schedule config is required for scheduled triggers"}), 400

        interval = schedule.get('interval')
        unit = schedule.get('unit', 'minutes')
        if unit ==  'seconds':
            eta = datetime.now() + timedelta(seconds=interval)
        elif unit == 'minutes':
            eta = datetime.utcnow() + timedelta(minutes=interval)
        elif unit == 'hours':
            eta = datetime.utcnow() + timedelta(hours=interval)
        else:
            return jsonify({"error": "Invalid schedule unit"}), 400
        print(new_trigger.id)
        
        fire_trigger.apply_async((new_trigger.id,), eta=eta,is_manual=True)
        print('hiited')
    return TriggerSchema().jsonify(new_trigger), 201

@trigger_blueprint.route('/test', methods=['POST'])
def test_trigger():
    """
    Test a trigger manually without saving it permanently.
    """
    data = request.json
    trigger_type = data.get('type')
    payload = data.get('payload', {})

    if trigger_type not in ['scheduled', 'api']:
        return jsonify({"error": "Invalid trigger type"}), 400

    # Log the manual trigger
    fire_trigger.delay(None, payload=payload, is_manual=True)
    return jsonify({"message": "Trigger test initiated."}), 200
