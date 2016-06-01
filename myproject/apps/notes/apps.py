from django.apps import AppConfig


class NotesConfig(AppConfig):
    name = 'notes'
    verbose_name = "Notes API"

    def ready(self):
        super(NotesConfig, self).ready()
