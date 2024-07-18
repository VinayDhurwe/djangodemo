from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('palindrome/', views.palindrome, name='palindrome'),
    path('fibonacci/', views.fibonacci, name='fibonacci'),
    path('reverse/', views.reverse_string, name='reverse'),  # Update to use reverse_string
]
