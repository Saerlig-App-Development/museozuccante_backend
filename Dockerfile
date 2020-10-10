FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

COPY . .

RUN pip install --upgrade pip
RUN pip install -r museozuccante/requirements.txt

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "museozuccante", "--bind", "unix:/opt/services/djangoapp/socket/django.sock", "museozuccante.wsgi:application", "--workers", "2"]