import django_filters
import json

from .models import *

class TypeFilter(django_filters.FilterSet):

    class Meta:
        model = AuthUser
        fields = ('user_type')