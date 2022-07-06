from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AuthUser, UserAdmin)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(OCS)
admin.site.register(ADPD)


