from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
# Create your views here.





class OrederView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({'status':"ok"})
    