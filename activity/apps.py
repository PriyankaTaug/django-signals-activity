from django.apps import AppConfig

class ActivityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activity'

    def ready(self):
        import activity.signals  # Ensure this is correctly importing signals
