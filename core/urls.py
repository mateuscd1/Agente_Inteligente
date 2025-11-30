from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('chat/', views.chat, name='chat'),
    path('upload/', views.upload_view, name='upload'),
    path('documento/<int:pk>/', views.document_detail, name='document_detail'),
    path('search/', views.search_view, name='search'),
    path('resumo/<int:pk>/', views.resumo_view, name='resumo'),
]
