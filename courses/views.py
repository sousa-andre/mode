from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.utils.translation import gettext_lazy as _, gettext

from mode.mixins import MultipleObjectFilterMixin
from classes.models import Course


class CourseCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'courses.manage_view_course'
    model = Course
    fields = [
        'name',
        'short_name',
        'type'
    ]
    success_message = _('The course was successfully updated.')
    success_url = reverse_lazy('courses:list')


class CourseList(PermissionRequiredMixin, MultipleObjectFilterMixin, ListView):
    permission_required = 'courses.manage_view_course'
    filter_columns = [
        'name',
        'type'
    ]
    model = Course
    fields = [
        'name',
        'short_name',
        'type'
    ]
    context_object_name = 'courses'
    paginate_by = 15


class CourseUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'courses.manage_view_course'
    model = Course
    fields = [
        'name',
        'short_name',
        'type'
    ]
    success_message = _('The course was successfully created.')
    context_object_name = 'course'


class CourseDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'courses.manage_view_course'
    model = Course
    success_url = reverse_lazy('courses:list')

    def post(self, request, *args, **kwargs):
        messages.success(request, gettext('The course was successfully removed.'))
        return super().post(request, *args, **kwargs)
