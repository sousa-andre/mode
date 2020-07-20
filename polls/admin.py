from django.contrib import admin

from .models import Question, Poll, Answer

admin.site.register([Question, Poll, Answer])
