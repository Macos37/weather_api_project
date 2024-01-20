FROM python:3.10

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=weather_api_project.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]