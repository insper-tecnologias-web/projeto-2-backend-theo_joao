from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/cadastro', views.cadastro),
    path('api/login', views.login),
    path('api/favoritos/<str:nome>', views.favoritos),
    path('api/adicionaFavorito', views.adicionaFavorito),
]