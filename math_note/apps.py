from django.apps import AppConfig


class MathConfig(AppConfig):
    name = 'math'
    verbose_name = 'math_note'
    def ready(self):
        from matcher.background_tasks import close_timeout_games
        from matcher.models import FourPlayerGame
        # check if a player is not responding every 5 seconds
        close_timeout_games(FourPlayerGame, repeat=5)