from django.urls import path
from .import views




urlpatterns = [
    path('', views.UserRegistrationView.as_view(), name='user'),
    path('login/', views.LoginUserAPIView.as_view(), name='Login'),
]


