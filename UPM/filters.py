import django_filters
import json

from .models import *

class RoomFilter(django_filters.FilterSet):

    capacity = django_filters.RangeFilter()

    class Meta:
        model = Room
        fields = ('college','building','room_type','capacity')