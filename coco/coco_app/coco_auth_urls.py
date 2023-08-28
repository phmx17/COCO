from django.urls import path
from . import auth_views as views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('not_authorized/', views.not_authorized, name='not_authorized'),
    path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
]

