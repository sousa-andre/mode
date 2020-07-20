from django.contrib.auth.models import Group
from django.test import TestCase

from accounts.models import User
from classes.models import Class, ClassSubject
from events.models import Event
from studygroups.models import StudyGroup
from subjects.models import Subject


class ModeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = User.objects.create_user(email='student@email.com', password='1234')
        cls.student.groups.add(Group.objects.get(pk=1))
        cls.teacher = User.objects.create_user(email='teacher@email.com', password='1234')
        cls.teacher.groups.add(Group.objects.get(pk=2))
        cls.secretary = User.objects.create_user(email='secretary@email.com', password='1234')
        cls.secretary.groups.add(Group.objects.get(pk=3))
        cls.director = User.objects.create_user(email='director@email.com', password='1234')
        cls.director.groups.add(Group.objects.get(pk=4))

        cls.admin = User.objects.create_superuser(email='admin@email.com', password='1234')
        cls.user = User.objects.create_user(email='user@email.com', password='1234')

    @classmethod
    def get_user_for_group(cls, group_id):
        if group_id == 1:
            return cls.student
        elif group_id == 2:
            return cls.teacher
        elif group_id == 3:
            return cls.secretary
        elif group_id == 4:
            return cls.director
