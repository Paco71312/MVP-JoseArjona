from django.urls import path
from arbol import views
urlpatterns = [
    path('crear-familiar/<str:nombre>/<str:apellido>/<int:edad>/', views.crear_familiar),
    path('ver-familiar/', views.ver_familiar),
]