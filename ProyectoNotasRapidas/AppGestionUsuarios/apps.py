from django.apps import AppConfig


class AppGestionUsuariosConfig(AppConfig):
   # default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppGestionUsuarios'

    def ready(self):
        import AppGestionUsuarios.signals
