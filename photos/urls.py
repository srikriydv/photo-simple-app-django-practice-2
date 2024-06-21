from django.urls import path
from . import views
urlpatterns = [
    path("", views.gallery, name='gallery'),
    path("add-photo/<str:pk>", views.addPhoto, name='add-photo'),
    path("view-photo", views.viewPhoto, name='view-photo'),
    
    
]
