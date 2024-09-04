# Используем официальный базовый образ Python
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
#RUN  apt-get update && apt-get install -y \
#    libpq-dev python-dev-is-python3

# Устанавливаем зависимости Python
#COPY config/requirements/requirements.txt /app/

COPY config/requirements/requirements.txt /app/

RUN pip install -r requirements.txt

# Copy the project to the work directory
COPY . /app/


# Команда для запуска Gunicorn
CMD ["sh", "-c", "./wait-for-it.sh local_db:5432 -- python manage.py migrate && gunicorn --bind 0.0.0.0:8000 config.wsgi:application"]

