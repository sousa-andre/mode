from django.test import TestCase
from django.urls import reverse, resolve

from ..views import EventList, EventCreate, EventUpdate, EventDelete


class TestUrls(TestCase):
    def test_event_list_url_is_resolved(self):
        url = reverse('events:list')
        self.assertEquals(resolve(url).func.view_class, EventList)

    def test_event_create_url_is_resolved(self):
        url = reverse('events:create')
        self.assertEquals(resolve(url).func.view_class, EventCreate)

    def test_event_update_url_is_resolved(self):
        url = reverse('events:update', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, EventUpdate)

    def test_event_delete_url_is_resolved(self):
        url = reverse('events:delete', kwargs={'pk': 0})
        self.assertEquals(resolve(url).func.view_class, EventDelete)
