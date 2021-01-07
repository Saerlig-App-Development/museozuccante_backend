FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/services/djangoapp/src/museozuccante
WORKDIR /opt/services/djangoapp/src/museozuccante

RUN pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "museozuccante", "--bind", ":8000", "museozuccante.wsgi:application", "--workers", "2"]