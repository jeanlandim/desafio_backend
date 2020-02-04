from .views import *
from django.urls import path, include, re_path

urlpatterns = [
        path('api-textos/',ApiList.as_view(),name='api-textos'),
        path('api-textos/<pk>',ApiListItems.as_view(),name='api-textos'),
        path('', busca, name='busca') 
]

