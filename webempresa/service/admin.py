from django.contrib import admin
from service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

# Register your models here.
admin.site.register(Service, ServiceAdmin)
