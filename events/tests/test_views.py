from django.urls import reverse

from mode.tests import ModeTestCase


class TestViews(ModeTestCase):
    def setUp(self):
        self.events_list_url = reverse('events:list')
        self.events_create_url = reverse('events:create')
        self.events_update_url = reverse('events:update', kwargs={'pk': 1})
        self.events_delete_url = reverse('events:delete', kwargs={'pk': 1})

    def test_events_list_GET_no_login(self):
        response = self.client.get(self.events_list_url)
        self.assertEquals(response.status_code, 302)

    def test_events_list_GET_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.get(self.events_list_url)
        self.assertEquals(response.status_code, 200)

    def test_events_create_GET_as_student(self):
        self.client.force_login(self.get_user_for_group(1))
        response = self.client.get(self.events_create_url)
        self.assertEquals(response.status_code, 403)

    def test_events_create_GET_as_teacher(self):
        self.client.force_login(self.get_user_for_group(2))
        response = self.client.get(self.events_create_url)
        self.assertEquals(response.status_code, 403)

    def test_events_create_GET_as_secretary(self):
        self.client.force_login(self.get_user_for_group(3))
        response = self.client.get(self.events_create_url)
        self.assertEquals(response.status_code, 403)

    def test_events_create_GET_as_director(self):
        self.client.force_login(self.get_user_for_group(4))
        response = self.client.get(self.events_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_form.html')

    def test_events_update_GET_as_student(self):
        self.client.force_login(self.get_user_for_group(1))
        response = self.client.get(self.events_update_url)
        self.assertEquals(response.status_code, 403)

    def test_events_delete_GET_as_teacher(self):
        self.client.force_login(self.get_user_for_group(2))
        response = self.client.get(self.events_update_url)
        self.assertEquals(response.status_code, 403)

    def tests_events_delete_GET_as_secretary(self):
        self.client.force_login(self.get_user_for_group(3))

