from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .views import AllPostview

class AllPost(APITestCase):
        def setUp(self):
            self.factory = APIRequestFactory()

            self.view = AllPostview.as_view()
            self.url = reverse('posts')

        def test_all_post(self):
              request = self.factory.get(self.url)

              response = self.view(request)

              self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # response = self.client.get(reverse('posts'))

        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # self.assertEqual(response.data['message'], 'all post')


    