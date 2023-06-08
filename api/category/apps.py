from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 👇👇 name field has to be equal to the name as in settings.py
    name = 'api.category'
