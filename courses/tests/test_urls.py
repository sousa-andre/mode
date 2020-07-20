from django.test import TestCase
from django.urls import reverse, resolve

from courses.views import CourseList, CourseCreate, CourseUpdate, CourseDelete


class TestUrls(TestCase):
    def test_course_list_url_is_resolved(self):
        url = reverse('courses:list')
        self.assertEquals(resolve(url).func.view_class, CourseList)

    def test_course_create_url_is_resolved(self):
        url = reverse('courses:create')
        self.assertEquals(resolve(url).func.view_class, CourseCreate)

    def test_course_update_url_is_resolved(self):
        url = reverse('courses:update', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, CourseUpdate)

    def test_course_delete_url_is_resolved(self):
        url = reverse('courses:delete', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, CourseDelete)
