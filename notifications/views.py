from django.shortcuts import get_object_or_404, redirect

from notifications.models import Notification


def notification_click_handler(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    Notification.objects.filter(id=notification_id).delete()
    if notification.redirect_url:
        return redirect(notification.redirect_url)
    else:
        return redirect('home')
