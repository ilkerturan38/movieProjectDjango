
from ast import Expression
from cProfile import label
from dataclasses import field
from random import choices
from django.forms import ChoiceField
import django_filters
from django_filters import CharFilter,DateFilter,ChoiceFilter
from .models.movie import movie

class movieFilter(django_filters.FilterSet):

    ozel_list=(
        ('ascending',"A-Z Sırala"),
        ('descending',"Z-A Sırala"),
    )

    start_date=DateFilter(field_name="date",lookup_expr="gte")
    end_date=DateFilter(field_name="date",lookup_expr="lte")
    ordering=ChoiceFilter(label="İşlem",choices=ozel_list,method="filter_by_order")
    class Meta:
        model = movie
        fields = ["genre","language","image_quality","date",]


    def filter_by_order(self, queryset,name,value):
        expression = 'title' if value == 'ascending' else '-title'
        return queryset.order_by(expression)


