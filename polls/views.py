from threading import Thread

from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods
from django.forms import modelformset_factory, formset_factory
from django.views.generic import ListView, DetailView, DeleteView

from notifications.utils import create_notification
from polls.forms import PollCreationForm, QuestionAnswerForm
from polls.models import Poll, Question, Answer


@require_http_methods(['GET', 'POST'])
@permission_required('polls.manage_view_poll', raise_exception=True)
def poll_create(request):
    QuestionFormSet = modelformset_factory(Question, fields=('content', ), extra=2)

    if request.method == 'POST':
        poll_form = PollCreationForm(request.POST)
        questions_formset = QuestionFormSet(request.POST, queryset=None)

        if poll_form.is_valid() and questions_formset.is_valid():
            poll = poll_form.save()
            for question_form in questions_formset:
                question_form.instance.poll_id = poll.id
            questions_formset.save()

            threads = []
            for user in Group.objects.get(id=1).user_set.all():
                t = Thread(
                    target=create_notification,
                    args=(
                        'New poll was created',
                        'A new poll was created. Please proceed to vote.',
                        reverse('polls:vote', kwargs={'poll_id': poll.id}),
                    ),
                    kwargs={'user': user},
                )
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()

            messages.success(request, _('The poll was successfully created.'))
            return redirect('polls:list')

    else:
        poll_form = PollCreationForm()
        questions_formset = QuestionFormSet(queryset=Question.objects.none())

    return render(request, 'polls/poll_form.html', {
        'poll_form': poll_form,
        'questions_formset': questions_formset
    })


@require_http_methods(['GET', 'POST'])
@permission_required('polls.vote_poll')
def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if Group.objects.get(pk=1) not in request.user.groups:
        messages.error(request, _('Only students can vote'))
        return redirect('home')
    if Answer.objects.filter(question__poll=poll, user=request.user).count() > 0:
        messages.error(request, _('You already voted for this poll.'))
        return redirect('home')

    QuestionAnswerFormSet = formset_factory(QuestionAnswerForm, extra=poll.questions.count())

    if request.method == 'POST':
        question_formset = QuestionAnswerFormSet(request.POST)
        for question, form in zip(poll.questions.all(), question_formset):
            form.fields['score'].label = question.content

        if question_formset.is_valid():
            for question, form in zip(poll.questions.all(), question_formset):
                form.instance.question_id = question.id
                form.instance.user_id = request.user.id
                form.save()
            messages.success(request, _('The poll was successfully updated.!'))
        return redirect('polls:list')

    else:
        question_formset = QuestionAnswerFormSet()
        for question, form in zip(poll.questions.all(), question_formset):
            form.fields['score'].label = question.content

    return render(request, 'polls/poll_vote_form.html', {
        'poll': poll,
        'question_formset': question_formset,
    })


class PollList(PermissionRequiredMixin, ListView):
    permission_required = 'polls.manage_view_poll'
    model = Poll
    context_object_name = 'polls'


class PollDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'polls.manage_view_poll'
    model = Poll
    context_object_name = 'poll'


class PollDelete(DeleteView):
    permission_required = 'polls.manage_view_poll'
    model = Poll

    def post(self, request, *args, **kwargs):
        messages.success(request, _('The poll was successfully removed.'))
        return super().post(request, *args, **kwargs)
