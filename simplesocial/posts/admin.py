from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    fields = ['user','message','group']
    search_fields = ['user','message','group']
    list_filter = ['user','message','group']
    list_display = ['user','message','group']
    list_editable = ['message','group']

admin.site.register(models.Post,PostAdmin)
