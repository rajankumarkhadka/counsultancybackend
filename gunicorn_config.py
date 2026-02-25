# Gunicorn configuration file
# Place this file in the project root or use with: gunicorn -c gunicorn_config.py

import os
from pathlib import Path

# Get the absolute path to the project directory
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR

# Server socket configuration
bind = "0.0.0.0:8000"  # Change to unix socket for production: "unix:{PROJECT_DIR}/gunicorn.sock"
backlog = 2048

# Worker processes
workers = os.cpu_count() or 4
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 120
keepalive = 5

# Logging
accesslog = str(PROJECT_DIR / "logs" / "gunicorn_access.log")
errorlog = str(PROJECT_DIR / "logs" / "gunicorn_error.log")
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = "counsultancybackend"

# Server hooks
pre_fork = None
post_fork = None
pre_exec = None
post_exec = None
pre_request = None

def post_request(worker, req, environ, resp):
    pass

# Reload on code changes (development only, disable in production)
reload = False

# Enable daemon mode (for manual management, disable if using systemd)
daemon = False

# Security
umask = 0
user = None  # Set to 'www-data' for production
group = None  # Set to 'www-data' for production

# WSGI application
wsgi_app = "counsultancybackend.wsgi:application"
pythonpath = str(BASE_DIR)

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(str(PROJECT_DIR / "logs" / "gunicorn_access.log")), exist_ok=True)
