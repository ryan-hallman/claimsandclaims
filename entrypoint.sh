#!/bin/sh

# Ensures that the database is up before issuing the create_db command

if [ "$DATABASE" = "postgres" ] || [ "$DATABASE" = "mysql" ]; then
    echo "Waiting for $DATABASE..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "Database $DATABASE started"
fi

if [ "$FLASK_ENV" = "development" ]
then
    echo "Dropping database and creating the database tables..."
    python manage.py create_db
    echo "Tables created"
fi

exec "$@"