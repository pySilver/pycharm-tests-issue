from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "Users API"

    def ready(self):
        super(UsersConfig, self).ready()
