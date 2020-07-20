from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext, gettext_lazy as _
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from mode.mixins import MultipleObjectFilterMixin
from subjects.models import Subject


class SubjectCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'subjects.manage_view_subject'
    model = Subject
    fields = [
        'name',
        'short_name'
    ]
    success_url = reverse_lazy('subjects:list')
    success_message = _('The subject was successfully created.')


class SubjectList(MultipleObjectFilterMixin, PermissionRequiredMixin, ListView):
    permission_required = 'subjects.manage_view_subject'
    filter_columns = [
        'name',
        'short_name'
    ]
    model = Subject
    context_object_name = 'subjects'
    paginate_by = 10


class SubjectUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'subjects.manage_view_subject'
    model = Subject
    fields = [
        'name',
        'short_name'
    ]
    success_message = _('The subject was successfully updated.')


class SubjectDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'subjects.manage_view_subject'
    model = Subject
    success_url = reverse_lazy('subjects:list')
    context_object_name = 'subject'

    def post(self, *args, **kwargs):
        messages.success(self.request, gettext('The subject was successfully removed.'))
        return super().post(*args, **kwargs)

