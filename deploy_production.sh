#!/bin/bash
# Production deployment helper script
# Usage: ./deploy_production.sh

set -e

echo "═══════════════════════════════════════════════════════════════"
echo "  Django Production Deployment Helper"
echo "═══════════════════════════════════════════════════════════════"

# Check if .env exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env and update the values:"
    echo "  cp .env.example .env"
    echo "  nano .env"
    exit 1
fi

# Check if DEBUG is False
if grep -q "DEBUG=True" .env; then
    echo "❌ Error: DEBUG is set to True in .env"
    echo "Set DEBUG=False for production!"
    exit 1
fi

echo "✅ .env file found and DEBUG is False"

# Export .env variables
export $(cat .env | grep -v '#' | xargs)

# Verify critical environment variables
if [ -z "$SECRET_KEY" ]; then
    echo "❌ Error: SECRET_KEY not set in .env"
    exit 1
fi

if [ -z "$ALLOWED_HOSTS" ]; then
    echo "❌ Error: ALLOWED_HOSTS not set in .env"
    exit 1
fi

if [ -z "$DB_NAME" ]; then
    echo "❌ Error: Database credentials not set in .env"
    exit 1
fi

echo "✅ All required environment variables are set"

# Check if virtual environment exists
if [ ! -d "env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env
fi

# Activate virtual environment
source env/bin/activate

echo "✅ Virtual environment activated"

# Install/upgrade requirements
echo "📦 Installing requirements..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create logs directory
mkdir -p logs

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  ✅ Deployment preparation complete!"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "  1. Create superuser (if needed):"
echo "     python manage.py createsuperuser"
echo ""
echo "  2. Start Gunicorn:"
echo "     gunicorn counsultancybackend.wsgi:application \\"
echo "       --bind 0.0.0.0:8000 --workers 4"
echo ""
echo "  3. Or use systemd (see PRODUCTION_DEPLOYMENT.md)"
echo ""
echo "  4. Configure Nginx as reverse proxy (see PRODUCTION_DEPLOYMENT.md)"
echo ""
echo "  5. Setup SSL with Let's Encrypt:"
echo "     sudo certbot certonly --nginx -d yourdomain.com"
echo ""
echo "For complete setup guide, see: PRODUCTION_DEPLOYMENT.md"
echo ""
