import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_email_celery.settings')

app = Celery('django_email_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
