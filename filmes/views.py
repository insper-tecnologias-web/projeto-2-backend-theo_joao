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
        print('request', request.data)
        usuario = request.data
        nome = usuario['login']
        senha = usuario['senha']

        try:
            us = Usuario.objects.get(login=nome)
            print('us', us.favoritos)
            if nome == us.login and senha == us.senha:
                print('dados do usuario batem')
                return JsonResponse({'message' : 'Login efetuado'})
            else:
                return JsonResponse({'message' : 'Senha está incorreta'})
        except Usuario.DoesNotExist:
            return JsonResponse({'message' : 'Usuário não existente'})
        
@api_view(['GET'])
def favoritos(request, nome):
    print('nome', nome)
    try:
        us = Usuario.objects.get(login=nome)
        filmes_favoritos = us.favoritos.all()
        
        titulos_favoritos = [filme.title for filme in filmes_favoritos]
        generos_favoritos = [filme.generos for filme in filmes_favoritos]
        streamings_favoritos = [filme.streamings for filme in filmes_favoritos]
        links_favoritos = [filme.links for filme in filmes_favoritos]

        infos_favoritos = {
            'titulos': titulos_favoritos,
            'generos': generos_favoritos,
            'streamings': streamings_favoritos,
            'links': links_favoritos,
        }

        print('Filmes favoritos do usuário:', infos_favoritos)
        return JsonResponse({'filmes_favoritos': infos_favoritos})
    except Usuario.DoesNotExist:
        return JsonResponse({'message': 'Não há usuário'})

        
        
@api_view(['POST'])
def adicionaFavorito(request):
    if request.method == 'POST':
        info = request.data
        nome = info['login']
        titulo = info['titulo']
        generos = info['generos']
        streamings = info['streamings']  # Corrigi o nome do campo
        links = info['links']

        # Verificar se o usuário existe
        try:
            usuario = Usuario.objects.get(login=nome)
        except Usuario.DoesNotExist:
            return JsonResponse({'message': 'Usuário não encontrado'})

        # Verificar se o filme já está nos favoritos do usuário
        if usuario.favoritos.filter(title=titulo).exists():
            return JsonResponse({'message': 'Filme já está nos favoritos'})

        # Criar e salvar o novo filme
        novo_filme = Filme(title=titulo, generos=generos, streamings=streamings, links=links)
        novo_filme.save()

        # Adicionar o novo filme aos favoritos do usuário
        usuario.favoritos.add(novo_filme)

        return JsonResponse({'message': 'Filme adicionado aos favoritos'})

    return JsonResponse({'message': 'Requisição inválida'})
