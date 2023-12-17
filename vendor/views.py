from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .models import Vendor
import uuid
from rest_framework import permissions,authentication

# from .serializers import UserSerializer
# Create your views here.


class RegisterView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        query_set = Vendor.objects.all()
        serilizer_class = RegisterSerializer(query_set, many = True)
        
        return Response(serilizer_class.data)
    

    def post(self, request):
        print("entered this")
        
        data = request.data
        serializer_instance = RegisterSerializer(data=data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        return Response(serializer_instance.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request,pk):
        data = request.data['vendor_code']
        instance = Vendor.objects.filter(vendor_code = data).first()

        serilizer_instance = RegisterSerializer(data=data)

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]