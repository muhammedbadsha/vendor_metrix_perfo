from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,authentication

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

from django.shortcuts import render

from .models import CustomUser
from .serilizers import UserRegistrationSerializer
# Create your views here.


class UserRegistrationView(APIView):
    # authentication_classes = [authentication.BaseAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserRegistrationSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Your custom authentication logic goes here
        # For example, you might check a token in the request header

        token = request.headers.get('Authorization')
        if not token:
            return None

        try:
            user = User.objects.get(username=token)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such user')

        return (user, None)

class LoginUser(APIView):
    def post(self, request):
        
        return Response()