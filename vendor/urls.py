from django.urls import path
from .import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'vendor', views.RegisterSerializer,basename = 'vendor')
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', views.RegisterView.as_view(), name='registration')

]
# urlpatterns+=router.urls