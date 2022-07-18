import django_filters
import json

from .models import *

class RoomFilter(django_filters.FilterSet):

    capacity = django_filters.RangeFilter()
    dbuild = {}
    list_build = []
    for build in Building.objects.all():
        if build.college.name in dbuild:
            dbuild[build.college.name].append(build.name)
        else:
            dbuild[build.college.name] = [build.name]
        list_build.append((build.name,build.name))

    colleges = [str(col) for col in College.objects.all()]

    colleges = json.dumps(colleges)
    build = json.dumps(dbuild)

    class Meta:
        model = Room
        fields = ('college','building','room_type','capacity')