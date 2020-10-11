docker-compose build
docker-compose run djangoapp museozuccante/manage.py makemigrations
docker-compose run djangoapp museozuccante/manage.py migrate
docker-compose run djangoapp museozuccante/manage.py collectstatic --no-input
docker-compose run djangoapp museozuccante/manage.py createsuperuser
