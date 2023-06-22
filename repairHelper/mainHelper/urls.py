from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


# ustawianie patterrnów w urlach

urlpatterns = [
    path('', views.default, name='default'),
    path('home/', views.home, name='home'),
    path('show_spares/', views.showSpares, name='showSpares'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('create_repair/', views.createRepair, name='createRepair'),
    path('create_customer/', views.createCustomer, name='createCustomer'),
    path('add_spare/', views.addSpare, name='addSpare'),
    path('add_device_type/', views.addDeviceType, name='addDeviceType'),
    path('repair/<int:id>/', views.repairDetail, name='repair-detail'),
    path('repair/<int:id>/edit/', views.repairEdit, name='repair-edit'),
]
