import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, DeleteView

from notifications.utils import create_notification
from .forms import CommentCreationForm
from .models import Post, Interaction


class PostList(PermissionRequiredMixin, ListView):
    permission_required = 'forum.create_view_post'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for index, post in enumerate(context['posts']):
            post.is_liked = bool(post.interactions.filter(user=self.request.user).count() >0)
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'forum.create_view_post'
    model = Post
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, gettext('The post was created successfully.'))
        return super().form_valid(form)


class PostCommentsView(PermissionRequiredMixin, View):
    permission_required = 'forum.create_view_post'
    model = Post
    form_class = CommentCreationForm
    template_name = 'forum/post_comment_detail.html'
    context_object_name = 'post'

    def get_object(self):
        return self.model.objects.filter(id=self.kwargs['pk']).first()

    def get(self, request, *args, **kwargs):
        comment_form = self.form_class()

        return render(self.request, self.template_name, {
            self.context_object_name: self.get_object(),
            'form': comment_form
        })

    def post(self, *args, **kwargs):
        comment_form = self.form_class(self.request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = self.request.user
            comment_form.instance.post_id = self.kwargs['pk']
            comment_form.save()
            messages.success(self.request, gettext('The comment was successfully added.'))
            create_notification(
                gettext('New post comment'),
                gettext('Someone added a comment into your forum post'),
                redirect_url=reverse('forum:detail', kwargs={'pk': self.kwargs.get('pk')}),
                user=comment_form.instance.post.author
            )
            return redirect('forum:detail', pk=1)

        return render(self.request, self.template_name, {
            self.context_object_name: self.get_object(),
            'forum': comment_form
        })


class PostDelete(DeleteView):
    model = Post
    context_object_name = 'post'

    def dispatch(self, request, *args, **kwargs):
        if not (request.user == self.get_object().author or request.user.has_perm('forum.delete_post')):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, gettext('Post successfully deleted.'))
        return super().post(request, *args, **kwargs)



@require_POST
@csrf_exempt
@login_required
def post_action(request):
    data = json.loads(request.body)

    action = Interaction.objects.filter(post_id=data['postId'], user=request.user)
    if action:
        action.delete()
        return HttpResponse(status=204)
    else:
        Interaction.objects.create(
            type=data['type'],
            user=request.user,
            post_id=data['postId']
        )
        return HttpResponse(status=200)
