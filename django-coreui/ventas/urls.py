from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_venta, name='crear_venta'),
    path('exitosa/<int:venta_id>/', views.venta_exitosa, name='venta_exitosa')
]