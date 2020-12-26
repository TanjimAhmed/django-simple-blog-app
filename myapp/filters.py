import django_filters
from django_filters import CharFilter
from .models import *

class BlogFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Blog
        fields = ['title','category']