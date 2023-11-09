from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import Http404
from .models import Filme, Usuario
from .serializers import FilmeSerializer
from .serializers import UsuarioSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['POST'])
def cadastro(request):
    if request.method == 'POST':
        novo_usuario = request.data

        usuarios = Usuario.objects.all()

        nomes_usuarios = []
        for u in usuarios:
            nomes_usuarios.append(str(u))

        if novo_usuario['login'] not in nomes_usuarios:
            login = novo_usuario['login']
            senha = novo_usuario['senha']
            usuario = Usuario(login = login, senha = senha)
            usuario.save()

        else:
            return JsonResponse({'message' : 'esse usuario ja existe'})
        

    return JsonResponse({'message': 'Data received successfully'})

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        print(request)
        novo_usuario = request.data

       #teste
        try:
            us = Usuario.objects.get(login=novo_usuario['login'])
        except Usuario.DoesNotExist:
            raise Http404()
        print(us)
        #fim do teste
        

    return JsonResponse({'message': 'Data received successfully'})