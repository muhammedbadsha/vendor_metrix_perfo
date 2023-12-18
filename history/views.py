from rest_framework import generics
from .models import PerformanceRecord
from .serializers import PerformanceRecordSerializer

class PerformanceRecordListCreateView(generics.ListCreateAPIView):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer

class PerformanceRecordRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer

# Add other views as needed
