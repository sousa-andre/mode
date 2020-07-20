from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext
from django.utils.translation.trans_null import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import FormMixin, ProcessFormView, DeleteView

from classes.forms import ClassForm, ClassStudentAddition, ClassSubjectsForm
from accounts.models import User
from mode.mixins import MultipleObjectFilterMixin
from notifications.utils import create_notification
from .models import Class


class ClassList(PermissionRequiredMixin, MultipleObjectFilterMixin, ListView):
    permission_required = 'classes.manage_view_class'
    filter_columns = [
        'year',
        'grade',
        'abc',
        'director__first_name',
        'director__last_name',
        'director__email',
        'course__short_name'
    ]
    model = Class
    context_object_name = 'classes'
    paginate_by = 10
    ordering = ['-year']
    success_url = reverse_lazy('classes:list')


class ClassCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'classes.manage_view_class'
    model = Class
    form_class = ClassForm
    context_object_name = 'classes'
    success_message = _('The class successfully created.')
    success_url = reverse_lazy('classes:list')


class ClassUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'classes.manage_view_class'
    model = Class
    form_class = ClassForm
    success_message = _('The class was successfully updated.')
    success_url = reverse_lazy('classes:list')


class ClassDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'classes.manage_view_class'
    model = Class
    context_object_name = 'class'
    success_url = reverse_lazy('classes:list')

    def post(self, request, *args, **kwargs):
        messages.success(request, gettext('Class was successfully removed.'))
        return super().post(request, *args, **kwargs)


class ClassStudentsAddList(PermissionRequiredMixin, FormMixin, DetailView, ProcessFormView):
    permission_required = 'classes.manage_view_class'
    model = Class
    form_class = ClassStudentAddition
    context_object_name = 'class'
    object = None
    template_name = 'classes/class_student_detail.html'

    def form_valid(self, form):
        klass = self.get_object()
        if form.user.groups.filter(id=1).count() < 1:
            messages.warning(self.request, gettext("There's no student with the following email."))
            return redirect(self.get_success_url())

        klass.students.add(form.user)
        messages.success(self.request, gettext('The Student was successfully added.'))
        create_notification(
            gettext('Added to a new class'),
            gettext('You have been added to the class {}.').format(klass),
            redirect_url=reverse('klass:class-detail'),
            user=form.user
        )
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['class_id'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self):
        return reverse('classes:students', kwargs={'pk': self.kwargs['pk']})


@permission_required('classes.manage_view_class')
@require_http_methods(['GET', 'POST'])
def class_student_delete(request, class_pk, user_pk):
    if request.method == 'GET':
        return render(request, 'classes/class_student_remove.html')
    else:
        klass = Class.objects.get(pk=class_pk)
        user = User.objects.get(pk=user_pk)

        klass.students.remove(user)

        messages.success(request, _('The student was successfully removed.'))
        return redirect('classes:students', pk=class_pk)


@permission_required('classes.manage_view_class')
@require_http_methods(['GET', 'POST'])
def class_subjects(request, class_pk):
    klass = Class.objects.get(pk=class_pk)

    if request.method == 'GET':
        form = ClassSubjectsForm(class_pk)

    else:
        form = ClassSubjectsForm(class_pk, data=request.POST)
        if form.is_valid():
            messages.success(request, gettext('The subject was successfully added.'))
            form.instance.klass_id = class_pk
            form.save()
            return redirect('classes:subjects', class_pk=class_pk)

    return render(request, 'classes/class_subjects_list_create.html', {
        'form': form,
        'class': klass
    })
