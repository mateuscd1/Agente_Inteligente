from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('chat/', views.chat, name='chat'),
    path('upload/', views.upload_view, name='upload'),
    path('search/', views.search_view, name='search'),
    path('resumo/<int:pk>/', views.resumo_view, name='resumo'),
     # login/logout usando views prontas do Django (template customizado abaixo)
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    # outras rotas...
    path("documento/<int:doc_id>/editar/", views.editar_documento, name="editar_documento"),
    path("documento/<int:doc_id>/excluir/", views.excluir_documento, name="excluir_documento"),
    path("chat/api/", views.chat_api, name="chat_api"),

    
]
