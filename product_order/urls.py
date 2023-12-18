from django.urls import path
from .import views

urlpatterns = [
    path('',views.OrederView.as_view(),name='oreder_product'),
    path('orders/', views.OrderProductListCreateView.as_view(), name='order-product-list-create'),
    path('orders/<int:pk>/',views.OrderProductRetrieveUpdateView.as_view(), name='order-product-retrieve-update'),
    
]