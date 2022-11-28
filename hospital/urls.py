from django.urls import path
from hospital import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('appointment/', views.appoinment, name='appointment'),
    path('profile', views.profile, name='profile')
]
