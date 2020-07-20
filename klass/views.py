from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.utils.translation import gettext_lazy as _, gettext

from classes.models import ClassSubject, Class
from .forms import AppointmentForm
from .models import File, Appointment
from .mixins import ClassSubjectTeacherRequired


@login_required
def class_detail(request):
    if Class.objects.filter(Q(students=request.user) | Q(subjects__teacher=request.user)).count() < 1:
        raise Http404()

    return render(request, 'klass/class_detail.html')


class ClassSubjectDetail(DetailView):
    model = ClassSubject
    context_object_name = 'subject'
    template_name = 'klass/subject_files.html'


class ClassSubjectFileCreate(ClassSubjectTeacherRequired, CreateView):
    model = File
    fields = [
        'title',
        'description',
        'file',
    ]

    def form_valid(self, form):
        messages.success(self.request, gettext('The file was successfully added.'))
        form.instance.created_by = self.request.user
        form.instance.subject_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('klass:subject-detail', kwargs={'pk': self.kwargs.get('pk')})


class ClassSubjectFileUpdate(ClassSubjectTeacherRequired, SuccessMessageMixin, UpdateView):
    model = File
    fields = [
        'title',
        'content'
    ]
    success_message = _('The file was successfully updated.')


class ClassSubjectFileDelete(ClassSubjectTeacherRequired, DeleteView):
    model = File

    def post(self, request, *args, **kwargs):
        messages.success(request, gettext('The file was successfully removed'))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('klass:subject-detail', kwargs={'pk': self.kwargs.get('pk')})


class AppointmentCreate(ClassSubjectTeacherRequired, SuccessMessageMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.subject_id = self.kwargs.get('pk')
        messages.success(self.request, gettext('The appointment was successfully created.'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('klass:subject-detail', kwargs={'pk': self.kwargs.get('pk')})


class AppointmentUpdate(ClassSubjectTeacherRequired, SuccessMessageMixin, UpdateView):
    model = Appointment
    fields = [
        'title',
        'content',
        'starts_at',
        'ends_at'
    ]
    context_object_name = 'appointment'
    success_message = _('The appointment was successfully updated.')


class AppointmentDelete(ClassSubjectTeacherRequired, DeleteView):
    model = Appointment

    def post(self, request, *args, **kwargs):
        messages.success(request, gettext('The appointment was successfully removed.'))
        return super().post(request, *args, **kwargs)

