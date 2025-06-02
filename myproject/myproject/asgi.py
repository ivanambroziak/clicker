import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Використовуємо стандартний ASGI без Channels, оскільки WebSocket не використовується
application = get_asgi_application()