from django import forms
from django.contrib.auth.models import Group

from classes.models import Class, ClassSubject
from accounts.models import User


class ClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['director'].queryset = Group.objects.get(pk=2).user_set.all()

    class Meta:
        model = Class
        fields = [
            'year',
            'abc',
            'grade',
            'course',
            'director',
        ]


class ClassStudentAddition(forms.Form):
    email = forms.EmailField()

    def __init__(self, class_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_id = class_id
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if email is not None:
            try:
                self.user = User.objects.get(email=cleaned_data['email'])
            except User.DoesNotExist:
                raise forms.ValidationError('Nenhum aluno encontrado com o e-mail especificado', code='invalid')

        return cleaned_data


class ClassSubjectsForm(forms.ModelForm):
    def __init__(self, class_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Group.objects.get(pk=2).user_set.all()
        self.class_id = class_id

    class Meta:
        model = ClassSubject
        fields = [
            'subject',
            'teacher'
        ]

    def clean(self):
        cleaned_data = super().clean()
        teacher = cleaned_data.get('teacher')
        subject = cleaned_data.get('subject')

        try:
            self.Meta.model.objects.get(teacher=teacher, subject=subject, klass_id=self.class_id)
            raise forms.ValidationError('Já existe esse professor com a mesma disciplina', code='not-unique')
        except self.Meta.model.DoesNotExist:
            pass

        return cleaned_data
