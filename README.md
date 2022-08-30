# Eskiz-SMS-Testing
Eskiz SMS sending via code generators 


set eskiz email and password in sms->helper.py


# SetUp project your machine
    python -v venv venv
    source venv/bin/activate
    pip install -r requirement.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 
    Open localhost:8000/sms/send 
 
# Celery set up
    celery -A project worker --beat
          - celery is the CLI command
          - A project references the django configuration folder cfehome where celery.py lives.
          - worker means our task offloader is running
          - --beat turns this running instance of Celery into a beat process as well (ie runs scheduled items not just offloaded tasks).
    celery -A project beat #f we just wanted to run a beat worker on it's own we can omit --beat above and, in another terminal instance, run:
    celery -A project worker -l info --beat #Tasks 
    celery -A project woker --beat -l info #Run Worker & Beat Server

# At least 3 Processes Running (at least)
    python manage.py runserver
    celery -A cfehome worker --beat -l info
    redis-server
