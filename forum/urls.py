from django.urls import path

from forum.views import PostList, PostCreate, PostCommentsView, post_action, PostDelete

app_name = 'forum'
urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('criar/', PostCreate.as_view(), name='create'),
    path('<int:pk>/', PostCommentsView.as_view(), name='detail'),
    path('<int:pk>/remover/', PostDelete.as_view(), name='delete'),

    path('api/gostar/', post_action, name='urls')
]
