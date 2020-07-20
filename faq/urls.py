from django.urls import path

from faq.views import TopicList, TopicCreate, TopicDelete, TopicUpdate

app_name = 'faq'
urlpatterns = [
    path('', TopicList.as_view(), name='list'),
    path('criar/', TopicCreate.as_view(), name='create'),
    path('<int:pk>/atualizar/', TopicUpdate.as_view(), name='update'),
    path('<int:pk>/eliminar/', TopicDelete.as_view(), name='delete')
]
