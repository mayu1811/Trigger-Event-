# File: app/config.py
import os

class Config:
    # Database URI for PostgreSQL (update accordingly)
    SQLALCHEMY_DATABASE_URI = 'postgresql://mayur:Panda%40123@localhost/event_trigger_platform'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Celery Configuration for Redis Broker and Backend
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Optional: Enable logging for Celery tasks
    CELERY_TASK_TRACK_STARTED = True
    CELERY_TASK_TIME_LIMIT = 30 * 60  # Example time limit for tasks in seconds (30 minutes)

    # Optional: You may want to define the Redis configuration for other components as well
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0

    # Ensure Redis server is running properly (debugging)
    CELERYD_LOG_COLOR = True
    CELERYD_LOG_FILE = '/var/log/celery/celery.log'  # Set appropriate log path
