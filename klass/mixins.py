from django.core.exceptions import PermissionDenied
from django.http import Http404

from .models import ClassSubject


class ClassSubjectTeacherRequired:
    def dispatch(self, request, *args, **kwargs):
        try:
            subject = ClassSubject.objects.get(id=self.kwargs.get('pk'))
            if request.user != subject.teacher:
                raise PermissionDenied()
        except ClassSubject.DoesNotExist:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)

