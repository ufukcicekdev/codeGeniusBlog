from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from notification.models import *
from user_profile.models import *
import os
from dotenv import load_dotenv

load_dotenv()

def send_notification_email(notification):
    to_email = [notification.user.email]  # Kullanıcının e-posta adresi
    from_email = os.getenv('EMAIL_HOST_USER')  # Gönderen e-posta adresi
    context = {
        'notification': notification,
    }

    if notification.notification_types == 'Blog':
        subject = "New Blog Notification"
        html_template = 'email/blog_notification_template.html'
    elif notification.notification_types == 'Like':
        subject = "New Like Notification"
        html_template = 'email/like_notification_template.html'
    elif notification.notification_types == 'Follow':
        subject = "New Follow Notification"
        html_template = 'email/follow_notification_template.html'
    else:
        subject = "New Notification"
        html_template = 'email/notification_template.html'  # Varsayılan şablon

    # HTML ve düz metin şablonlarını oluşturma
    html_message = render_to_string(html_template, context)
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)