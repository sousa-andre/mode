from django.urls import path

from courses.views import CourseCreate, CourseUpdate, CourseDelete, CourseList

app_name = 'courses'
urlpatterns = [
    path('', CourseList.as_view(), name='list'),
    path('criar/', CourseCreate.as_view(), name='create'),
    path('<int:pk>/atualizar/', CourseUpdate.as_view(), name='update'),
    path('<int:pk>/eliminar/', CourseDelete.as_view(), name='delete')
]
