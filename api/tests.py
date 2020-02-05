from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Api

class TestApi(APITestCase):

    def setUp(self):
        self.url = '/api-textos/'
        self.dados = {"titulo":"Turivius"
        ,"texto":"Sua nova forma de fazer pesquisa jurídica"}
        self.cliente_de_teste = APIClient()
    def test_post(self):
        response = self.cliente_de_teste.post(self.url,self.dados,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_get(self):
        response = self.cliente_de_teste.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_busca(self):
        response_titulo = self.cliente_de_teste.get(self.url+'?titulo='+"Turivius")
        response_texto = self.cliente_de_teste.get(self.url+'?texto='+"Sua")
        self.assertEqual(response_titulo.status_code, status.HTTP_200_OK)
        self.assertEqual(response_texto.status_code, status.HTTP_200_OK)
