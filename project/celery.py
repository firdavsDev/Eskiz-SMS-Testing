import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# taskimiz har 30 sekunda run qilish uchun configuratsiya
app.conf.beat_schedule = {
    'run-every-30-seconds': {
        'task': 'sms.tasks.send_sms_to_user',
        'schedule': 30.0, #every 30 seccond run our task function(send_sms_to_user)
        # 'args': 9989*******
    },
}

