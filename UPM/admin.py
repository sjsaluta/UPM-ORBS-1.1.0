from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Building)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Term)
admin.site.register(Schedule)
admin.site.register(ScheduleFile)
admin.site.register(Equipment)
admin.site.register(Contact)

