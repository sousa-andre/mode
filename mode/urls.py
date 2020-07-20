from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings

from accounts.views import student_registration, profile_update


urlpatterns = [
    path('admin/', admin.site.urls),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(), name='logout'),
    path('registar/', student_registration, name='student-registration'),
    path('', RedirectView.as_view(pattern_name='events:list'), name='home'),
    path('perfil/', profile_update, name='profile'),

    path('utilizadores/', include('accounts.urls'), name='users'),
    path('turmas/', include('classes.urls'), name='classes'),
    path('turma/', include('klass.urls'), name='class'),
    path('grupos-de-estudo/', include('studygroups.urls'), name='studygroups'),
    path('forum/', include('forum.urls'), name='forum'),
    path('eventos/', include('events.urls'), name='activities'),
    path('cursos/', include('courses.urls'), name='courses'),
    path('disciplinas/', include('subjects.urls'), name='subjects'),
    path('faq/', include('faq.urls'), name='faq'),
    path('votacoes/', include('polls.urls'), name='polls'),
    path('notificacoes/', include('notifications.urls'), name='notifications'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
