from django.test import TestCase
from django.urls import reverse, resolve

from klass.views import class_detail, ClassSubjectDetail, ClassSubjectFileCreate, ClassSubjectFileUpdate, \
    ClassSubjectFileDelete, AppointmentCreate, AppointmentUpdate, AppointmentDelete


class TestUrls(TestCase):
    def test_class_detail_url_is_resolved(self):
        url = reverse('klass:class-detail')
        self.assertEquals(resolve(url).func, class_detail)

    def test_class_subject_detail_is_resolved(self):
        url = reverse('klass:subject-detail', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, ClassSubjectDetail)

    def test_class_subject_file_create(self):
        url = reverse('klass:subject-file-create', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, ClassSubjectFileCreate)

    def test_class_subject_file_update(self):
        url = reverse('klass:subject-file-update', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, ClassSubjectFileUpdate)

    def test_class_subject_file_delete(self):
        url = reverse('klass:subject-file-delete', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, ClassSubjectFileDelete)

    def test_class_subject_appointment_create(self):
        url = reverse('klass:appointment-create', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, AppointmentCreate)

    def test_class_subject_appointment_update(self):
        url = reverse('klass:appointment-update', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, AppointmentUpdate)

    def test_class_subject_appointment_delete(self):
        url = reverse('klass:appointment-delete', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, AppointmentDelete)
