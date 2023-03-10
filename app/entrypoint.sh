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
export DJANGO_SUPERUSER_PASSWORD=admin
python manage.py createsuperuser --no-input --username admin --email admin@admin.fr

exec "$@"