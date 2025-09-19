from django.urls import path
from . import views


urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    
    path('create/', views.resume_create, name='resume_create'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
    path("register/", views.register_view, name="register"),
    path('<int:pk>/delete/', views.resume_delete, name='resume_delete'),
    path('resumes/<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('resumes/', views.resume_list, name='resume_list'),
    path('resumes/create/', views.resume_create, name='resume_create'),
    path("templates/", views.templates_list, name="templates_list"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('profile/', views.profile, name='profile'),
]

