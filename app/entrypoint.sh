#!/bin/sh

if [ "$ENGINE" = "django_iris" ]
then
    echo "Waiting for IRIS..."

    while ! nc -z $HOST $PORT; do
      sleep 0.5
    done

    echo "IRIS started"
fi

# python manage.py flush --no-input
python manage.py migrate

exec "$@"