from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _, gettext
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Topic


class TopicList(LoginRequiredMixin, ListView):
    model = Topic
    context_object_name = 'topics'


class TopicCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'faq.add_topic'
    model = Topic
    fields = [
        'title',
        'content'
    ]
    success_url = reverse_lazy('faq:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, gettext('The topic was successfully created.'))
        return super().form_valid(form)


class TopicUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'faq.change_topic'
    model = Topic
    context_object_name = 'topic'
    success_message = _('The topic was successfully updated.')
    fields = [
        'title',
        'content'
    ]


class TopicDelete(DeleteView):
    permission_required = 'faq.delete_topic'
    model = Topic
    context_object_name = 'topic'

    def post(self, request, *args, **kwargs):
        messages.success(request, _('The topic was successfully removed.'))
        return super().post(request, *args, **kwargs)
