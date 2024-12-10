from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login_user, name='login'),  # Login page
    path('session/', views.session, name='session'),  # Session input form page
    path('session_start/', views.session_start, name='session_start'),
    path('generate_report/', views.generate_report, name='generate_report'),
]
