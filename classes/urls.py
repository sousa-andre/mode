from django.urls import path

from classes.views import ClassList, ClassUpdate, ClassStudentsAddList, ClassCreate, class_student_delete, \
    class_subjects, ClassDelete

app_name = 'classes'
urlpatterns = [
    path('', ClassList.as_view(), name='list'),
    path('criar/', ClassCreate.as_view(), name='create'),
    path('<int:pk>/atualizar/', ClassUpdate.as_view(), name='update'),
    path('<int:pk>/eliminar/', ClassDelete.as_view(), name='delete'),
    path('<int:pk>/', ClassStudentsAddList.as_view(), name='students'),
    path('<int:class_pk>/alunos/<int:user_pk>/remover/', class_student_delete, name='student-delete'),
    path('<int:class_pk>/disciplinas/', class_subjects, name='subjects'),

]
