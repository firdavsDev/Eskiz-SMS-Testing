from django.db import models

# Create your models here.

class SMSToken(models.Model):
    name = models.CharField(max_length=50)
    token = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    expires_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SMS Token'
        verbose_name_plural = 'SMS Tokens'
        ordering = ['-id']


class SMSLog(models.Model):
    phone = models.CharField(max_length=20)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'SMS Log'
        verbose_name_plural = 'SMS Logs'
        ordering = ['-id']
