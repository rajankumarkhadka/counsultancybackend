#!/bin/bash
# Docker helper script for common operations

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}\n"
}

print_success() {
    echo -e "${GREEN}✅  $1${NC}"
}

print_error() {
    echo -e "${RED}❌  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️   $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️   $1${NC}"
}

# Check if Docker is installed
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed!"
        echo "Install Docker from: https://docs.docker.com/get-docker/"
        exit 1
    fi
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed!"
        echo "Install Docker Compose from: https://docs.docker.com/compose/install/"
        exit 1
    fi
    print_success "Docker and Docker Compose are installed"
}

# Build images
build() {
    print_header "Building Docker Images"
    docker-compose build "$@"
    print_success "Build complete!"
}

# Start services
start() {
    print_header "Starting Services"
    docker-compose up -d
    print_success "Services started!"
    print_info "Waiting for services to be healthy..."
    sleep 5
    status
}

# Stop services
stop() {
    print_header "Stopping Services"
    docker-compose down
    print_success "Services stopped!"
}

# View logs
logs() {
    docker-compose logs -f "$@"
}

# Run migrations
migrate() {
    print_header "Running Database Migrations"
    docker-compose exec web python manage.py migrate --noinput
    print_success "Migrations complete!"
}

# Create superuser
superuser() {
    print_header "Creating Superuser"
    docker-compose exec web python manage.py createsuperuser
}

# Collect static files
static() {
    print_header "Collecting Static Files"
    docker-compose exec web python manage.py collectstatic --noinput --clear
    print_success "Static files collected!"
}

# Show service status
status() {
    print_header "Service Status"
    docker-compose ps
}

# Health check
health() {
    print_header "Health Check"
    
    print_info "Checking web service..."
    if docker-compose exec -T web curl -f http://localhost:8000/health/ &>/dev/null; then
        print_success "Web service is healthy"
    else
        print_error "Web service is not responding"
    fi
    
    print_info "Checking database..."
    if docker-compose exec db pg_isready -U "${DB_USER:-counsultancy_user}" &>/dev/null; then
        print_success "Database is healthy"
    else
        print_error "Database is not responding"
    fi
    
    print_info "Checking Nginx..."
    if docker-compose exec -T nginx nginx -t &>/dev/null; then
        print_success "Nginx configuration is valid"
    else
        print_error "Nginx configuration has errors"
    fi
}

# View database shell
dbshell() {
    print_header "Connecting to Database"
    docker-compose exec db psql -U "${DB_USER:-counsultancy_user}" -d "${DB_NAME:-counsultancy_db}"
}

# Backup database
backup() {
    print_header "Backing Up Database"
    BACKUP_FILE="backup_$(date +%Y%m%d_%H%M%S).sql"
    docker-compose exec -T db pg_dump -U "${DB_USER:-counsultancy_user}" "${DB_NAME:-counsultancy_db}" > "$BACKUP_FILE"
    print_success "Database backed up to: $BACKUP_FILE"
}

# Restore database
restore() {
    if [ -z "$1" ]; then
        print_error "Usage: $0 restore <backup_file>"
        exit 1
    fi
    
    if [ ! -f "$1" ]; then
        print_error "Backup file not found: $1"
        exit 1
    fi
    
    print_header "Restoring Database"
    docker-compose exec -T db psql -U "${DB_USER:-counsultancy_user}" -d "${DB_NAME:-counsultancy_db}" < "$1"
    print_success "Database restored from: $1"
}

# Shell access
shell() {
    print_header "Django Shell"
    docker-compose exec web python manage.py shell_plus
}

# Clean up
clean() {
    print_header "Cleaning Up Docker Resources"
    print_warning "This will remove containers, images, and volumes!"
    read -p "Are you sure? (yes/no) " -n 3 -r
    echo
    if [[ $REPLY =~ ^[Yy][Ee][Ss]$ ]]; then
        docker-compose down -v
        docker system prune -af
        print_success "Cleanup complete!"
    else
        print_info "Cleanup cancelled"
    fi
}

# Initialize
init() {
    print_header "Initializing Docker Environment"
    
    if [ ! -f .env ]; then
        print_warning ".env file not found"
        read -p "Copy from .env.example? (yes/no) " -n 3 -r
        echo
        if [[ $REPLY =~ ^[Yy][Ee][Ss]$ ]]; then
            cp .env.example .env
            print_success ".env created from .env.example"
            print_warning "Please update .env with your production values!"
        fi
    else
        print_success ".env file exists"
    fi
    
    build
    start
    migrate
    static
    
    print_success "Initialization complete!"
    print_info "Next steps:"
    echo "  1. Create admin user: $0 superuser"
    echo "  2. View logs: $0 logs"
    echo "  3. Check health: $0 health"
    echo "  4. Access admin: http://localhost:8000/admin/"
}

# Show help
help() {
    echo -e "${BLUE}Docker Helper Script${NC}"
    echo ""
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  init              Initialize Docker environment (build, start, migrate)"
    echo "  build            Build Docker images"
    echo "  start            Start services"
    echo "  stop             Stop services"
    echo "  restart          Restart services"
    echo "  status           Show service status"
    echo "  health           Check service health"
    echo "  logs [service]   View logs (web, db, nginx)"
    echo "  migrate          Run database migrations"
    echo "  static           Collect static files"
    echo "  superuser        Create Django superuser"
    echo "  shell            Access Django shell"
    echo "  dbshell          Access database shell"
    echo "  backup           Backup database"
    echo "  restore <file>   Restore database from backup"
    echo "  clean            Remove all containers and volumes"
    echo "  help             Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 init                  # Initialize everything"
    echo "  $0 logs web              # View web service logs"
    echo "  $0 backup                # Backup database"
    echo "  $0 restore backup_*.sql  # Restore from backup"
    echo ""
}

# Main script
main() {
    check_docker
    
    case "${1:-help}" in
        build)     build "${@:2}" ;;
        start)     start ;;
        stop)      stop ;;
        restart)   stop && start ;;
        status)    status ;;
        health)    health ;;
        logs)      logs "${@:2}" ;;
        migrate)   migrate ;;
        static)    static ;;
        superuser) superuser ;;
        shell)     shell ;;
        dbshell)   dbshell ;;
        backup)    backup ;;
        restore)   restore "$2" ;;
        clean)     clean ;;
        init)      init ;;
        help|--help|-h)  help ;;
        *)         print_error "Unknown command: $1" && help && exit 1 ;;
    esac
}

# Run main function
main "$@"
