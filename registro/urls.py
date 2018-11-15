from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('home2', views.home2, name='home2'),
    path('home3', views.home3, name='home3'),
    path('login', views.dologin, name = 'dologin'),
    path('telamotorista', views.telamotorista, name ='telamotorista'),
    path('telausuario', views.reservaformulario.as_view()),
    path('motoristaregistro', views.motoristaformulario.as_view()),
    path('usuarioregistro', views.usuarioformulario.as_view()),
    path('autenticacao', views.entraar),
    path('logout', views.dologout),
    path('oi', views.criar_user),
    path('deletar_rota/<int:id>', views.deletar_rota, name='deletar_rota'),

    #path('usuarioformulario', views.entrar),
    #path('cadastrar/', views.cadastrar_usuario),
]