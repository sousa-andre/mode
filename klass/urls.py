from django.urls import path

from .views import \
    class_detail, ClassSubjectDetail, ClassSubjectFileCreate, \
    ClassSubjectFileUpdate, ClassSubjectFileDelete, AppointmentCreate, AppointmentUpdate, AppointmentDelete

app_name = 'klass'
urlpatterns = [
    path('', class_detail, name='class-detail'),
    path('<int:pk>/ficheiros/', ClassSubjectDetail.as_view(), name='subject-detail'),
    path('<int:pk>/ficheiros/criar/', ClassSubjectFileCreate.as_view(), name='subject-file-create'),
    path('<int:pk>/ficheiros/atualizar/', ClassSubjectFileUpdate.as_view(), name='subject-file-update'),
    path('<int:pk>/ficheiros/remover/', ClassSubjectFileDelete.as_view(), name='subject-file-delete'),
    path('<int:pk>/agenda/criar/', AppointmentCreate.as_view(), name='appointment-create'),
    path('<int:pk>/agenda/atualizar', AppointmentUpdate.as_view(), name='appointment-update'),
    path('<int:pk>/agenda/remover', AppointmentDelete.as_view(), name='appointment-delete')
]
