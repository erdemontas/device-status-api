from .models import *
from django.contrib import admin


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name','id', 'created_at')

class StatusActivityAdmin(admin.ModelAdmin):
    list_display = ('device', 'status', 'modified_at')

admin.site.register(Device, DeviceAdmin)
admin.site.register(StatusActivity, StatusActivityAdmin)
