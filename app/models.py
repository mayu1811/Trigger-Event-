# File: app/models.py
from app import db

class Trigger(db.Model):
    __tablename__ = 'trigger'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    config = db.Column(db.JSON, nullable=False)  # Store schedule or API payload

class EventLog(db.Model):
    __tablename__ = 'eventlog'
    id = db.Column(db.Integer, primary_key=True)
    trigger_id = db.Column(db.Integer, db.ForeignKey('trigger.id'), nullable=True)
    triggered_at = db.Column(db.DateTime, nullable=False)
    payload = db.Column(db.JSON, nullable=True)
    state = db.Column(db.String(50), nullable=False)  # e.g., 'active', 'archived'
