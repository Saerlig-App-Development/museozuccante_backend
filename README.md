# Museo Zuccante

### Requirements

 - Docker version 19.03.8
 - docker-compose version 1.25.0
 
### Setup
* Automatic:
  * `./setup.sh` (setup.bat)

* Manual:
  * `docker-compose build`
  * `docker-compose run djangoapp museozuccante/manage.py makemigrations`
  * `docker-compose run djangoapp museozuccante/manage.py migrate`
  * `docker-compose run djangoapp museozuccante/manage.py collectstatic --no-input`
  * `docker-compose run djangoapp museozuccante/manage.py createsuperuser`

### Run
 - `docker-compose up`
 
### Update
* `docker-compose build`
* if models were changed:
  * `docker-compose run djangoapp museozuccante/manage.py makemigrations`
  * `docker-compose run djangoapp museozuccante/manage.py migrate `
  
### By
- [Leone Bacciu](https://github.com/LeoneBacciu)
- [Diego Caspi](https://github.com/diegocaspi)