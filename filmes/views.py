from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Filme
from .serializers import FilmeSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        filme = Filme.objects.get(id=note_id)
    except Filme.DoesNotExist:
        raise Http404()
    serialized_note = FilmeSerializer(filme)
    return Response(serialized_note.data)