docker start museozuccante_backend_djangoapp_1
docker exec -it museozuccante_backend_djangoapp_1 ./manage.py flush --no-input
docker exec -it museozuccante_backend_djangoapp_1 find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
docker exec -it museozuccante_backend_djangoapp_1 find . -path "*/migrations/*.pyc" -delete
docker exec -it museozuccante_backend_djangoapp_1 ./manage.py makemigrations
docker exec -it museozuccante_backend_djangoapp_1 ./manage.py migrate
docker exec -it museozuccante_backend_djangoapp_1 ./manage.py collectstatic --no-input
docker exec -it museozuccante_backend_djangoapp_1 ./manage.py createsuperuser
docker stop museozuccante_backend_djangoapp_1
