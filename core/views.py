from django.http import HttpResponse
from core.serializers import UploadedFileSerializer
from rest_framework import status
from .serializers import  *
from .models import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User



@api_view(['POST' , 'GET'])
@permission_classes([permissions.IsAuthenticated])
def upload_or_get(request):
    if request.method == 'POST':
        serializer = UploadedFileSerializer(data=request.data)
        #upload file to MINIO
        if serializer.is_valid():
            file = serializer.validated_data["file"]
            
            # get the format of file
            type = str(file).split(".")[1]

            serializer.save(user_id=request.user.id , size=file.size , type=type)
            return Response(serializer.data , status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        files = UploadedFile.objects.filter(user=request.user)
        serializer = UploadedFileSerializer(files , many=True)
        return Response(serializer.data)

    return Response("Something Went Wrong" , status=status.HTTP_400_BAD_REQUEST)

       
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_file(request , id):
    if request.method == 'DELETE':
        file = UploadedFile.objects.get(id=id)
        file.delete()
        return Response("Deleted successfully ! " )