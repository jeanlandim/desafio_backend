from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Api
from .serializers import ApiSerializer
from .filters import ApiFilter

class ApiList(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo','texto']
class ApiListItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
def busca(request):
    lista_de_textos = Api.objects.all()
    filtro_dos_textos = ApiFilter(request.GET, queryset=lista_de_textos)
    return render(request, 'index.html', {'busca': filtro_dos_textos})

