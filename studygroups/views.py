from threading import Thread

from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.utils.translation import gettext, gettext_lazy as _
from django.shortcuts import get_object_or_404, redirect

from notifications.utils import create_notification
from .models import StudyGroup


class StudyGroupList(PermissionRequiredMixin, ListView):
    permission_required = 'studygroups.view_studygroup'
    model = StudyGroup
    context_object_name = 'study_groups'


class StudyGroupCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'studygroups.create_studygroup'
    model = StudyGroup
    fields = [
        'name',
        'content',
        'related_subjects',
    ]
    success_message = _('The study group was successfully created.')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class StudyGroupUpdate(SuccessMessageMixin, UpdateView):
    model = StudyGroup
    fields = [
        'name',
        'content',
        'related_subjects'
    ]
    success_message = _('The study group was successfully updated.')
    context_object_name = 'study_group'

    def dispatch(self, request, *args, **kwargs):
        if not (self.get_object().created_by == self.request.user
                or request.user.has_perm('studygroup.update_delete_studygroup')):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class StudyGroupDelete(DeleteView):
    model = StudyGroup
    success_message = _('The study group was successfully deleted.')
    context_object_name = 'study_group'
    success_url = reverse_lazy('studygroups:list')

    def post(self, request, *args, **kwargs):
        if not (self.get_object().created_by == self.request.user
                or request.user.has_perm('studygroup.update_delete_studygroup')):
            raise PermissionDenied()

        messages.success(request, self.success_message)

        subject = gettext('One of the study groups you were participating in was deleted.')
        content = gettext('The group {group_name} was removed.')

        threads = []
        for user in self.get_object().participants.all():
            t = Thread(target=create_notification, args=(subject,), kwargs={
                'user': user,
                'content': content.format(group_name=self.get_object().name),
                'redirect_url': reverse('studygroups:list')
            })
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

        return super().post(request, *args, **kwargs)


@require_POST
@permission_required('studygroups.subscribe_studygroup')
def study_group_subscribe(request, study_group_id):
    study_group = get_object_or_404(StudyGroup, id=study_group_id)

    if study_group.participants.filter(id=request.user.id).count() > 0:
        study_group.participants.remove(request.user)
        messages.success(request, gettext('The study group subscription was successfully removed.'))
    else:
        study_group.participants.add(request.user)
        messages.success(request, gettext('The study group subscription was registered.'))
    return redirect('studygroups:list')
