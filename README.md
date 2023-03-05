# easy-meals-api

Nutrition management API

# Build & run commands

docker-compose build
docker-compose up

# Make migrations

docker-compose run app sh -c "python manage.py makemigrations {module}"

# Migrate the db

docker-compose run app sh -c "python manage.py migrate"

# Create superuser

docker-compose run app sh -c "python manage.py createsuperuser"

# Drop db

docker-compose exec db psql -U postgres -d postgres -c "DROP DATABASE app"

# Restart server after pulling latest changes from GitHub

docker-compose -f docker-compose-deploy.yml build app
docker-compose -f docker-compose-deploy.yml up --no-deps -d app
