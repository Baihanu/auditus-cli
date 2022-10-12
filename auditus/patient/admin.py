from django.contrib import admin
from auditus.patient.models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
