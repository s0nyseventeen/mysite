from django.apps import AppConfig


class PollsConfig(AppConfig):
    print(f'{dir()=}')
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
