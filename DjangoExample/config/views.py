from django.shortcuts import HttpResponse
from time import sleep

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)


class NoMethodExceptGetAllowed(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)


class NoPermissions(TestView):
    permission_classes = (IsAuthenticated, )


class InternalError(APIView):
    def get(self, request, *args, **kwargs):
        print(a)
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)
