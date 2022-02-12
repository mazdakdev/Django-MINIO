
from django.urls import path , include
from . import views

urlpatterns = [
    path('upload/' , views.upload_or_get , name="upload" ),
    path('upload/<int:id>' , views.delete_file , name="delete"), 
]