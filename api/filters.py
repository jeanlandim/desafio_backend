from .models import Api
import django_filters

class ApiFilter(django_filters.FilterSet):
    class Meta:
        model = Api
        fields = ['titulo','texto']

