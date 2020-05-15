from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer)
]