from django.contrib import admin
from . import models
# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    fields = ['name','slug','description']
    search_fields = ['name','slug','description']
    list_filter = ['name','slug']
    list_display = ['name','slug','description']
    list_editable = ['slug','description']

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group,GroupAdmin)
