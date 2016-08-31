from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

from e_users.models import UserDetail

class UserDetailAdmin(admin.ModelAdmin):

    def cost(obj):
        return "%s" % obj.cost
    def reading(obj):
        return "%s" % obj.reading
    def timestamp(obj):
        return "%s" % obj.timestamp
    def user(obj):
        return "%s" % obj.user

    user.short_description = 'User'
    cost.short_description = 'Cost'
    reading.short_description = 'Reading'
    timestamp.short_description = 'Time Stamp'

    list_display = (user,cost, reading, timestamp, )

admin.site.unregister(Group)
admin.site.register(UserDetail, UserDetailAdmin)
