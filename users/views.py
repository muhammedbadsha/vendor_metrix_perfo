from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import render

from .models import CustomUser
from .serilizers import UserRegistrationSerializer,LoginSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
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




class LoginUserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
#     def get(self, request):
#         return Response({"value":"login field"})
    """This api will handle login and return token for authenticate user."""
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        """We are reterving the token for authenticated user."""
                        token, created = Token.objects.get_or_create(user=user)

                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": {
                                       "Token" : token.key
                                       }
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)


# class CreateProductView(APIView):
#      def get(self, request):
#           product = Product.objects.all()

#           serializers_class = CreateProductSerializer(product,many=True)
#           return Response(serializers_class.data,status=status.HTTP_200_OK)
     

#      def post(self, request):
#         serializer = CreateProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
     


     
        