from django.urls import path

from polls.views import poll_create, poll_vote, PollList, PollDetail, PollDelete

app_name = 'polls'
urlpatterns = [
    path('', PollList.as_view(), name='list'),
    path('<int:pk>/', PollDetail.as_view(), name='detail'),
    path('criar/', poll_create, name='create'),
    path('<int:poll_id>/votar/', poll_vote, name='vote'),
    path('<int:pk>/apagar/', PollDelete.as_view(), name='delete')
]
