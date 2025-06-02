# Вихідний образ
FROM python:3.11-slim

# Встановлюємо системні залежності
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Робоча директорія в контейнері
WORKDIR /app

# Копіюємо залежності
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проєкт
COPY . .

# Створюємо директорії для медіа та статичних файлів
RUN mkdir -p media staticfiles

# Збираємо статичні файли
RUN python manage.py collectstatic --noinput

# Відкриваємо порт
EXPOSE 8000

# Запуск сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]