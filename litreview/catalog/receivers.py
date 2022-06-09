import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from catalog.models import Ticket


@receiver(pre_save, sender=Ticket)
def pre_save_image(sender, instance, *args, **kwargs):
    if not instance.pk:
        return False

    try:
        old_image = Ticket.objects.get(pk=instance.pk).image
        try:
            new_image = instance.image
        except:
            new_image = None
        if not old_image == new_image:
            if os.path.isfile(old_image.path):
                os.remove(old_image.path)
    except:
        pass
