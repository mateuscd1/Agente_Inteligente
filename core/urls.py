from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('chat/', views.chat, name='chat'),
    path('upload/', views.upload_view, name='upload'),
    path('documento/<int:pk>/', views.document_detail, name='document_detail'),
    path('search/', views.search_view, name='search'),
    path('resumo/<int:pk>/', views.resumo_view, name='resumo'),
     # login/logout usando views prontas do Django (template customizado abaixo)
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # outras rotas...

    
]
