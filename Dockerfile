# Используем официальный базовый образ Python
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости системы
#RUN apt-get update && apt-get install -y \
#    libpq-dev \
#    gcc \
#    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
#COPY config/requirements/requirements.txt /app/

COPY . /app/

RUN pip install -r config/requirements/requirements.txt

# Копируем проект в рабочую директорию

# Команда для запуска Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]