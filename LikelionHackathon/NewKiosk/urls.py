'''
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

from .views import CategoryViewSet,  ProductViewSet, OrderViewSet ,Product_OrderViewSet

from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('category', CategoryViewSet)
routers.register('product', ProductViewSet)
routers.register('order', OrderViewSet)
routers.register('product-order', Product_OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
]
'''
from django.urls import path,include
from django.contrib import admin
from NewKiosk import views

urlpatterns = [
    path('api/category/', views.CategoryListAPI.as_view()),
    path('api/product/', views.ProductListAPI.as_view()),
    path('api/order/', views.OrderListAPI.as_view()),
    path('api/product_order/', views.Product_OrderListAPI.as_view()),
]

# >>>>>>> d0e8621caf4320d5893cc650758fa79c26a5d49a
