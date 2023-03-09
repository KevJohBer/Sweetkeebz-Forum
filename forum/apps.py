from django.apps import AppConfig


class ForumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'


class UserConfig(AppConfig):
    default_auto_field = 'djago.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
