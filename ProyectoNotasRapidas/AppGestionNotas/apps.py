from django.apps import AppConfig


class AppGestionNotasConfig(AppConfig):
    name = 'AppGestionNotas'

    def ready(self):
        import AppGestionNotas.signals
