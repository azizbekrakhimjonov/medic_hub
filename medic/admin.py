from django.contrib import admin
from medic.models import *

class PatientAdmin(admin.ModelAdmin):
    list_display = ["id", "fullname", "age"]


admin.site.register(Patient, PatientAdmin)

