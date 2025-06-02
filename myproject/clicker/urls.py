from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('click/', views.click_button, name='click_button'),
    path('add_comment/', views.add_comment, name='add_comment'),
]