from django.contrib import admin
from auditus.exams.models import Reason

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
