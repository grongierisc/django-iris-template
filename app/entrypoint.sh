#!/bin/sh

if [ "$ENGINE" = "django_iris" ]
then
    echo "Waiting for IRIS..."

    while ! nc -z $HOST $PORT; do
      sleep 0.5
    done

    # make sure IRIS is ready
    sleep 5

    echo "IRIS started"
fi

# python manage.py flush --no-input
python manage.py migrate
# create superuser
python manage.py createsuperuser --no-input --username admin --email admin@admin.fr --password admin

exec "$@"