#!/bin/bash
# Entrypoint script for Django application

set -e

echo "Starting Django application..."

# Wait for database to be ready
if [ -n "$DB_HOST" ]; then
    echo "Waiting for PostgreSQL to be ready at $DB_HOST:$DB_PORT..."
    while ! nc -z "$DB_HOST" "${DB_PORT:-5432}" 2>/dev/null; do
        echo "PostgreSQL is unavailable - sleeping..."
        sleep 1
    done
    echo "PostgreSQL is ready!"
fi

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create logs directory with proper permissions
mkdir -p logs
chmod 755 logs

echo "Django setup complete. Starting server..."

# Execute the main command (Gunicorn by default)
exec "$@"
