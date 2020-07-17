from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('customers/', views.customers, name="customers"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>', views.updateCustomer, name="update_customer"),
    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account'),

    path('product/<str:pk>/', views.product, name="product"),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),
    path('products/', views.products, name="products"),

    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]