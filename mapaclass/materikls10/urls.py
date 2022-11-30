from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peluang/', views.peluang, name='peluang'),
    path('BarisandanDeret/', views.peluang, name='BarisandanDeret'),
    path('Eksponen/', views.peluang, name='Eksponen'),
    path('LogIn/', views.peluang, name='LogIn'),
    path('LogOut/', views.peluang, name='LogOut'),
    path('Referensi/', views.peluang, name='Referensi'),
    path('Statistika/', views.peluang, name='Statistika'),
    path('Profil/', views.peluang, name='Profil'),
    
]