from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.models import Notificaiton
from notification.sendmail import send_notification_email

@receiver(post_save, sender=Notificaiton)
def send_email_on_new_notification(sender, instance, **kwargs):
    if not instance.send_mail:
        send_notification_email(instance)
        instance.send_mail = True
        instance.save()
