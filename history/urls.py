from django.urls import path
from .views import PerformanceRecordListCreateView, PerformanceRecordRetrieveUpdateView



urlpatterns = [
    path('performance-records/', PerformanceRecordListCreateView.as_view(), name='performance-record-list-create'),
    path('performance-records/<int:pk>/', PerformanceRecordRetrieveUpdateView.as_view(), name='performance-record-retrieve-update'),
    # Add other paths as needed
]
