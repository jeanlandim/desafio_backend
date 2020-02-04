from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Api
from .serializers import ApiSerializer

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

