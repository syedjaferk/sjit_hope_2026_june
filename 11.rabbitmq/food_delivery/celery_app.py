from celery import Celery

celery_app = Celery("food", broker="pyamqp://guest:guest@rabbitmq//")
