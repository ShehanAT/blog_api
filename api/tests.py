from django.test import TestCase
from rest_framework.test import force_authenticate, APIRequestFactory
from .views import posts_view, ping_view 


class ApiTestCase(TestCase):
    
    def test_api_posts_returns_200(self):
        factory = APIRequestFactory()
        api_posts_url = '/api/posts/?tag=tech'
        request = factory.get(api_posts_url)
        response = posts_view(request)
        assert response.status_code == 200

    def test_api_ping_returns_200(self):
        factory = APIRequestFactory()
        api_ping_url = '/api/ping'
        request = factory.get(api_ping_url)
        response = ping_view(request)
        assert response.status_code == 200 
