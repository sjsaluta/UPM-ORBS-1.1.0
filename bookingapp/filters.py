import django_filters
import json

from .models import *


#Filtering the rooms
class BookingFilter(django_filters.FilterSet):

    class Meta:
        model = Booking
        fields = ('room','subject','faculty', 'booker', 'activity')

