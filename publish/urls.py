from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish, name="publish"),
    path('pdf/', views.flipbook, name="pdf"),
]