from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password_generator/<str:username>/', views.password_generator, name='password_generator'),
    path('logout/', views.logout, name='logout'),
]
