from rest_framework import serializers
from .models import Filme
from .models import Usuario


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['title', 'generos', 'streamings', 'links']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'login', 'senha', 'favoritos']