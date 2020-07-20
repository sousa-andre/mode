from django.urls import reverse

from courses.models import Course
from mode.tests import ModeTestCase


class TestViews(ModeTestCase):
    def setUp(self):
        course = Course.objects.create(name='Course Name', short_name='Short name', type=1)

        self.course_list_url = reverse('courses:list')
        self.course_create_url = reverse('courses:create')
        self.course_update_url = reverse('courses:update', kwargs={'pk': course.id})
        self.course_delete_url = reverse('courses:delete', kwargs={'pk': course.id})

    def test_course_list_GET_as_student(self):
        self.client.force_login(self.get_user_for_group(1))
        response = self.client.get(self.course_list_url)
        self.assertEquals(response.status_code, 403)

    def test_course_create_GET_as_teacher(self):
        self.client.force_login(self.get_user_for_group(2))
        response = self.client.get(self.course_create_url)
        self.assertEquals(response.status_code, 403)

    def test_course_create_GET_as_secretary(self):
        self.client.force_login(self.get_user_for_group(3))
        response = self.client.get(self.course_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_form.html')

    def test_course_create_GET_as_director(self):
        self.client.force_login(self.get_user_for_group(4))
        response = self.client.get(self.course_create_url)
        self.assertEquals(response.status_code, 200)

    def test_course_update_GET_as_student(self):
        self.client.force_login(self.get_user_for_group(1))
        response = self.client.get(self.course_update_url)
        self.assertEquals(response.status_code, 403)

    def test_course_update_GET_as_teacher(self):
        self.client.force_login(self.get_user_for_group(2))
        response = self.client.get(self.course_update_url)
        self.assertEquals(response.status_code, 403)

    def test_course_update_GET_as_secretary(self):
        self.client.force_login(self.get_user_for_group(3))
        response = self.client.get(self.course_update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_form.html')

    def test_course_update_GET_as_director(self):
        self.client.force_login(self.get_user_for_group(4))
        response = self.client.get(self.course_update_url)
        self.assertEquals(response.status_code, 200)

    def test_course_delete_GET_as_director(self):
        self.client.force_login(self.get_user_for_group(4))
        response = self.client.get(self.course_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_confirm_delete.html')
