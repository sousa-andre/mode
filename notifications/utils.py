from django.core.mail import send_mail

from .models import Notification


def create_notification(subject, content, html_content=None, redirect_url=None, *, user):
    if html_content is not None:
        send_mail(subject, message=content, html_message=html_content, from_email=None, recipient_list=(user.email,))

    notification = Notification.objects.create(title=subject, description=content, redirect_url=redirect_url, user=user)
    print('nt:', notification)
