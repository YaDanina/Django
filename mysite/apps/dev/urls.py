from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    re_path('hardware', views.hardware, name = 'hardware'),
    path('printers', views.printers, name = 'printers'), 
    path('delete/<int:hardware_id>', views.delete, name = 'delete'),
    path('update/<int:hardware_id>', views.update, name = 'update'),
    path('create', views.createHardware, name = 'createHardware'),
]