from django.urls import path

from .views import StudyGroupList, StudyGroupCreate, study_group_subscribe, StudyGroupUpdate, StudyGroupDelete

app_name = 'studygroups'
urlpatterns = [
    path('', StudyGroupList.as_view(), name='list'),
    path('criar/', StudyGroupCreate.as_view(), name='create'),
    path('<int:pk>/atualizar/', StudyGroupUpdate.as_view(), name='update'),
    path('<int:pk>/eliminar/', StudyGroupDelete.as_view(), name='delete'),
    path('<int:study_group_id>/subscribe/', study_group_subscribe, name='subscribe')
]
