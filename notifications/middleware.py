from .models import Notification


class NotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user_notifications = Notification.objects.filter(user=request.user) \
            if request.user.is_authenticated else None
        return self.get_response(request)
