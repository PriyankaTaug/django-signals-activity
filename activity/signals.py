import logging
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from django.utils.timezone import now

# Get custom logger
logger = logging.getLogger('activity_logger')  # Ensure this matches the logger name in settings.py

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    print(f"LOGIN SIGNAL TRIGGERED: {user.username} logged in")  # Terminal print
    logger.info(f"User {user.username} logged in at {now()}")  # Log file entry


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    logger.info(f"User {user.username} logged out at {now()}")
