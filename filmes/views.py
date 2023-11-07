from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Filme
from .serializers import FilmeSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET', 'POST'])
def cadastro(request, note_id):
    if request.method == 'POST':
        login = request.data.get('login')
        senha = request.data.get('senha')
        print('login', login)
        print('senha', senha)