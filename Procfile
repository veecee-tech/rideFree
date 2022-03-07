release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn book_a_ride.wsgi --log-file -