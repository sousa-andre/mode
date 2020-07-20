from django.urls import path

from .views import user_activation, UserCreate, UserUpdate, UserList

app_name = 'accounts'
urlpatterns = [
    path('ativar/<int:user_id>/<str:token>/', user_activation, name='activation'),
    path('criar/', UserCreate.as_view(), name='create'),
    path('<str:pk>/atualizar/', UserUpdate.as_view(), name='update'),

    path('', UserList.as_view(), name='list'),
]
