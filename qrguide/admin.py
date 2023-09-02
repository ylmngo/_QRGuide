from django.contrib import admin

from .models import Comments 

class CommentsAdmin(admin.ModelAdmin):
    fields = ["name", "department", "phone", "message"]

admin.site.register(Comments, CommentsAdmin)