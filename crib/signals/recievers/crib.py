from django.dispatch import receiver
from django.db.models.signals import pre_save

from crib.models.category import Category


@receiver(pre_save, sender=Category)
def add_current_user(sender, **kwargs):
    print(f"Signal received from {sender} with args: {kwargs}")

