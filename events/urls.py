from django.urls import path

from .views import (
    EventCreate,
    EventList,
    EventDetail,
    EventUpdate,
    EventDelete
)

app_name = 'events'
urlpatterns = [
    path('', EventList.as_view(), name='list'),
    path('<int:pk>/', EventDetail.as_view(), name='detail'),
    path('<int:pk>/atualizar/', EventUpdate.as_view(), name='update'),
    path('criar/', EventCreate.as_view(), name='create'),
    path('<int:pk>/eliminar/', EventDelete.as_view(), name='delete'),
]
