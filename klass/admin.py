from django.contrib import admin

from .models import Appointment, File


admin.site.register([Appointment, File])
