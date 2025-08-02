# profiles/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    When a new User is created, automatically create a Profile.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Ensure the related Profile is saved whenever the User is saved.
    Useful if you add fields later that depend on user updates.
    """
    # If profile exists, save it (avoid creating duplicates)
    if hasattr(instance, 'profile'):
        instance.profile.save()
