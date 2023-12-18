from django.urls import path
from .import views

urlpatterns = [
    path('',views.OrederView.as_view(),name='oreder_product'),
]
