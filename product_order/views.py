
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import OrderProduct
from .serializers import OrderProductSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response
from .serializers import OrderProductSerializer
from .models import OrderProduct
# Create your views here.





class OrederView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        order_product = OrderProduct.objects.all()
        serializer_class = OrderProductSerializer(order_product, many=True)

        return Response(serializer_class.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        serializer_class = OrderProductSerializer(data=data, many = False)
        if serializer_class.is_valid():
            serializer_class.save()

            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderProductListCreateView(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class OrderProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()