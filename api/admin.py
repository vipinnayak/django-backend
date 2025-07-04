from django.contrib import admin
from .models import Insurance  # make sure this is your model name

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'witnesses', 'police_report', 'loss_type', 'status')
