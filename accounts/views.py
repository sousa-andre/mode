from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import UpdateView, CreateView, ListView

from mode.mixins import MultipleObjectFilterMixin


from .models import User
from .forms import (
    UserRegistrationForm,
    AdminUserRegistrationForm,
    UserProfilePasswordUpdateForm,
    UserProfileUpdateForm
)
from .tokens import user_activation_token


@require_http_methods(['GET', 'POST'])
def student_registration(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
    else:
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.instance.is_active = False
            user = form.save()
            user.groups.add(Group.objects.get(id=1))

            html_content = render_to_string('accounts/mails/account_activation.html', {
                'user_id': form.instance.pk,
                'token': user_activation_token.make_token(form.instance)
            }, request)
            EmailMessage(
                gettext('Account Registration Confirmation'),
                html_content,
                to=[form.instance.email]
            ).send()

            messages.success(
                request,
                gettext('Account created successfully! Please check your email to confirm your account.')
            )
            return redirect('login')

    return render(request, 'accounts/registration.html', {
        'form': form
    })


class UserList(LoginRequiredMixin, UserPassesTestMixin, MultipleObjectFilterMixin, ListView):
    filter_columns = [
        'id',
        'first_name',
        'last_name',
        'email',
        'groups__name'
    ]
    model = User
    context_object_name = 'users'
    paginate_by = 15
    ordering = '-id'

    def test_func(self):
        return self.request.user.is_superuser


class UserCreate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = AdminUserRegistrationForm
    success_message = _('The user was successfully created.')
    success_url = reverse_lazy('accounts:list')

    def test_func(self):
        return self.request.user.is_superuser


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = User
    context_object_name = 'user_object'
    success_url = reverse_lazy('accounts:list')
    success_message = _('The user was successfully updated.')
    fields = [
        'first_name',
        'last_name',
        'email',
        'is_active',
        'groups',
    ]

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@require_http_methods(['GET', 'POST'])
def profile_update(request):
    if request.method == 'GET':
        profile_form = UserProfileUpdateForm(user=request.user)
        password_form = UserProfilePasswordUpdateForm(user=request.user)

    else:
        profile_form = UserProfileUpdateForm(user=request.user)
        password_form = UserProfilePasswordUpdateForm(user=request.user)

        if 'profile_form' in request.POST:
            profile_form = UserProfileUpdateForm(request.POST, request.FILES, user=request.user)

            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, gettext('The Profile was successfully updated.'))
                return redirect('profile')

        else:
            password_form = UserProfilePasswordUpdateForm(request.POST, user=request.user)

            if password_form.is_valid():
                password_form.save()
                messages.success(request, gettext('Password successfully updated.'))
                return redirect('profile')

    return render(request, 'accounts/profile_forms.html', {
        'profile_form': profile_form,
        'password_form': password_form
    })


@require_GET
def user_activation(request, user_id, token):
    user = get_object_or_404(User, id=user_id)
    if user_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, gettext('Account successfully activated.'))
    else:
        messages.error(request, gettext('Invalid activation link.'))
    return redirect('home')
