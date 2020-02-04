from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Api
from .serializers import ApiSerializer
from .filters import ApiFilter

class ApiList(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser, TokenHasReadWriteScope]
class ApiListItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser, TokenHasReadWriteScope]

def busca(request):
    lista_de_textos = Api.objects.all()
    filtro_dos_textos = ApiFilter(request.GET, queryset=lista_de_textos)

    return render(request, 'lista_dos_textos.html', {'busca': filtro_dos_textos})

