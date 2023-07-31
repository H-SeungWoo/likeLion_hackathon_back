from django.urls import path,include
from django.contrib import admin
from NewKiosk import views

urlpatterns = [
    path('api/category/', views.CategoryListAPI.as_view()),
    path('api/product/', views.ProductListAPI.as_view()),
    path('api/order/', views.OrderListAPI.as_view()),
    path('api/product_order/', views.Product_OrderListAPI.as_view()),
]

