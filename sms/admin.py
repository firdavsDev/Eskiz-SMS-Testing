from django.contrib import admin
from .models import SMSToken, SMSLog

# Register your models here.

class SMSTokenAdmin(admin.ModelAdmin):
    list_display = ['name', 'token']
    search_fields = ['name']

    @admin.display(description='SMSToken')
    def token(self, obj):
        return obj.content[:0]

admin.site.register(SMSToken, SMSTokenAdmin)


class SMSLogAdmin(admin.ModelAdmin):
    list_display = ['phone', 'message', 'status']
    search_fields = ['phone']
    list_editable = ['status']

admin.site.register(SMSLog, SMSLogAdmin)