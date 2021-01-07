# Museo Zuccante

### Requirements

 - Docker version 19.03.8
 - docker-compose version 1.25.0
 
### Setup
* Automatic:
  * `docker-compose build`
  * `./setup.sh` (setup.bat)


### Run
 - `docker-compose up`
 
### Update

* `docker-compose build`
* if models were changed:
  * `docker exec -it museozuccante_backend_djangoapp_1 ./manage.py makemigrations`
  * `docker exec -it museozuccante_backend_djangoapp_1 ./manage.py migrate`
* if static files were changed:
  * `docker exec -it museozuccante_backend_djangoapp_1 ./manage.py collectstatic --no-input`
  
### By
- [Leone Bacciu](https://github.com/LeoneBacciu)
- [Diego Caspi](https://github.com/diegocaspi)