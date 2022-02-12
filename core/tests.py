from django.test import TestCase
from django.http import response
from django.urls import reverse 
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import *
import json
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django_minio_backend import MinioBackend

        
class FilesTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user("someuser","1234pass")
        self.token = RefreshToken.for_user(user).access_token

    
    def test_read_files(self):
        token = self.token
        video = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")    
        response = self.client.post(reverse("upload") , {'file':video} , format="multipart" , **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

        response = self.client.get(reverse("upload") , **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        id = json.loads(response.content)[0]["id"]
        self.assertEqual( id , 1 )

    def test_delete_file(self):
        token = self.token
        video = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")    
        response = self.client.post(reverse("upload") , {'file':video} , format="multipart" , **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

        del_response = self.client.delete("/api/upload/1" ,  **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        self.assertEqual(del_response.status_code , status.HTTP_200_OK)
        
class MinioTestCase(TestCase):
    
    def test_minio_is_availabe(self):
        minio_available = MinioBackend().is_minio_available()  # An empty string is fine this time
        self.assertTrue(minio_available)
