from django.db.models import Q

from .models import Class, ClassSubject


class LatestClass:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        classes = Class.objects.all().order_by('-year')
        request.current_class_year = classes.values_list('year')[0][0] if classes.count() > 0 else -1
        if request.user.is_authenticated:
            request.user_subjects = ClassSubject.objects.filter(
                Q(klass__year=request.current_class_year),
                Q(teacher=request.user) | Q(klass__students=request.user)
            )
        else:
            request.user_subjects = None

        return self.get_response(request)
