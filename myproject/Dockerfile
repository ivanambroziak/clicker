FROM python:3.13-slim

# Встановлення системних залежностей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Робоча директорія
WORKDIR /app

# Копіювання requirements
COPY requirements.txt .

# Встановлення Python залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання коду додатку
COPY . .

# Створення директорій для медіа та статичних файлів
RUN mkdir -p media staticfiles

# Створення суперкористувача (опціонально)
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=admin123

# Виконання міграцій і збирання статичних файлів
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Відкриття порту
EXPOSE 8000

# Команда для запуску
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]