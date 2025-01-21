#!/bin/sh

# Wait for database to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
    sleep 0.1
done
echo "PostgreSQL started"

# Run migrations
python manage.py migrate_schemas --shared
python manage.py migrate_schemas

# Create superuser
python manage.py create_superuser

# Start server
python manage.py runserver 0.0.0.0:8000 