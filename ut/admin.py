from django.contrib import admin
from .models import User, Topic

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_blocked')
    search_fields = ('id', 'username')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_time')
    search_fields = ('id', 'name')

admin.site.register(User, UserAdmin)
admin.site.register(Topic, TopicAdmin)
