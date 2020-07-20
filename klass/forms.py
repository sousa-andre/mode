from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'title',
            'content',
            'happens_at',
            'starts_at',
            'ends_at'
        ]
        widgets = {
            'happens_at': forms.DateInput(attrs={'type': 'date'}),
            'starts_at': forms.TimeInput(attrs={'type': 'time'}),
            'ends_at': forms.TimeInput(attrs={'type': 'time'})
        }

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['starts_at'] > cleaned_data['ends_at']:
            raise ValidationError(_('The start time must be earlier than end time.'))

        return cleaned_data
