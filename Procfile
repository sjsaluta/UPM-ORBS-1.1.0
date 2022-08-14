release: python manage.py migrate
web: gunicorn accounts.wsgi --log-file=-
web: gunicorn bookingapp.wsgi 
web: gunicorn UPM.wsgi 