from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from social.models import Link 

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    
    def get_readonly_fields(self, request: HttpRequest, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ("key", "name")
        return ("created", "updated")

admin.site.register(Link, LinkAdmin)
