from django.contrib import admin
from .models import Pet, Report
# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'owner','pet_breed')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('pet', 'reportName', 'reportType')