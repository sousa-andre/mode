from django.urls import path

from notifications.views import notification_click_handler

app_name = 'notifications'
urlpatterns = [
    path('<int:notification_id>/clicar/', notification_click_handler, name='click')
]
