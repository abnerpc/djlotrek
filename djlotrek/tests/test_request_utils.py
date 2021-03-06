import os
import mock

from django.test import TestCase
from requests import RequestException

from django.test import RequestFactory

from djlotrek.request_utils import get_host_url
from djlotrek.aes import decode


class RequestUtilsTestCase(TestCase):

    def setUp(self):
        pass

    def test_get_host_url(self):
        """Our beloved get_host_url utility"""
        request_factory = RequestFactory()
        request = request_factory.get('/path')
        request.META['HTTP_HOST'] = 'localhost'
        host_url = get_host_url(request)
        self.assertEqual(host_url, 'http://localhost')

    def test_get_host_url_no_request(self):
        """Our beloved get_host_url utility"""
        host_url = get_host_url(None)
        self.assertEqual(host_url, None)