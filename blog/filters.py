# Filter based on image model
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ImageFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label="Title")
    user = django_filters.ModelChoiceFilter(label="Artist", queryset = User.objects.all())
    album = django_filters.ModelChoiceFilter(label="Album", queryset = Album.objects.all())
    id = django_filters.NumberFilter(label="ID")

    class Meta:
        model = Image
        fields = ['album', 'id', 'title', 'user']
