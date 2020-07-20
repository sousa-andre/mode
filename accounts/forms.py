from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import Group

from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class AdminUserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'groups',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            user.groups.add(*self.cleaned_data['groups'])
        return user


class UserProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, user, **kwargs):
        super().__init__(instance=user, *args, **kwargs)

    class Meta:
        model = User
        fields = [
            'picture',
            'first_name',
            'last_name',
            'email',
        ]


class UserProfilePasswordUpdateForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
            }
        )
