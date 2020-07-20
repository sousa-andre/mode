from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _, gettext
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .models import Event


class EventList(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'
    ordering = '-created_at'


class EventCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'events.manage_event'
    model = Event
    fields = [
        'title',
        'image',
        'content'
    ]
    success_message = _('The event was successfully created.')
    success_url = reverse_lazy('events:list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EventDetail(SuccessMessageMixin, DetailView):
    model = Event
    context_object_name = 'event'


class EventUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'events.manage_event'
    model = Event
    fields = [
        'title',
        'image',
        'content'
    ]
    context_object_name = 'event'
    success_message = _('The event was successfully updated.')

    def get_success_url(self):
        return reverse('events:detail', kwargs={'pk': self.kwargs['pk']})


class EventDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'events.manage_event'
    model = Event

    def post(self, request, *args, **kwargs):
        messages.success(request, gettext('The event was successfully removed.'))


