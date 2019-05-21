from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('magazine/', views.magazine, name="magazine" ),
    path('store/', views.store, name="store"),
]
