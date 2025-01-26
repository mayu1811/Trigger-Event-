# File: app/tasks/scheduler.py
from celery import Celery
from datetime import datetime, timedelta
from app import db
from app.models import EventLog, Trigger

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def fire_trigger(trigger_id, payload=None, is_manual=False):
    """
    Fire a trigger and log the event.
    :param trigger_id: ID of the trigger.
    :param payload: Optional payload for API triggers.
    :param is_manual: Indicates if this is a manual test.
    """
    trigger = Trigger.query.get(trigger_id)
    print(trigger.id)
    if trigger:
        log = EventLog(
            trigger_id=trigger.id,
            triggered_at=datetime.utcnow(),
            payload=payload,
            state='active'
        )
        if is_manual:
            log.payload = payload or {"info": "Manual test trigger"}
        db.session.add(log)
        db.session.commit()

        # Transition to "archived" state after 2 hours
        archive_time = datetime.utcnow() + timedelta(hours=2)
        cleanup_log.apply_async((log.id,), eta=archive_time)

@celery.task
def cleanup_log(log_id):
    """
    Archive and delete logs after their retention period.
    """
    log = EventLog.query.get(log_id)
    if log and log.state == 'active':
        log.state = 'archived'
        db.session.commit()

        # Schedule deletion after 46 hours
        delete_time = datetime.utcnow() + timedelta(hours=46)
        delete_log.apply_async((log.id,), eta=delete_time)

@celery.task
def delete_log(log_id):
    """
    Delete logs after 48 hours.
    """
    log = EventLog.query.get(log_id)
    if log:
        db.session.delete(log)
        db.session.commit()
