# myapp/apps.py

from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'apps'

    def ready(self):
        import apps.signals  # Import signals to ensure they are registered
