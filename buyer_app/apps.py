from django.apps import AppConfig

class BuyerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buyer_app'

    def ready(self):
        import buyer_app.signals
