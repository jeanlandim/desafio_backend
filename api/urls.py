from .views import *
from django.urls import path, include

urlpatterns = [
        path('api-textos/',ApiList.as_view(),name='api-textos'),
        path('api-textos/<pk>',ApiListItems.as_view(),name='api-textos')
]

