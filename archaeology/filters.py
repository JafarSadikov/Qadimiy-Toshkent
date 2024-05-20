import django_filters
from .models import Archaeology


class CategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    order = django_filters.CharFilter(field_name='order',
                                      lookup_expr='icontains')  # content nomli maydon uchun filtirlash

    class Meta:
        model = Archaeology
        fields = ['title', 'order']
