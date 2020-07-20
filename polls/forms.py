from django import forms

from polls.models import Poll, Question, Answer


class PollCreationForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = [
            'title',
            'description'
        ]


class QuestionAnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].required = True

    class Meta:
        model = Answer
        fields = [
            'score',
        ]

        widgets = {
            'score': forms.RadioSelect(choices=Answer.Choices, attrs={'required': True})
        }


