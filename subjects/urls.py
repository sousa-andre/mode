from django.urls import path

from subjects.views import SubjectList, SubjectCreate, SubjectDelete

app_name = 'subjects'
urlpatterns = [
    path('', SubjectList.as_view(), name='list'),
    path('criar/', SubjectCreate.as_view(), name='create'),
    path('<int:pk>/apagar/', SubjectDelete.as_view(), name='delete')
]
