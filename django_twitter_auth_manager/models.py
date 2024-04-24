from django.db import models
import time

class Access_token(models.Model):
    token_type = models.CharField(max_length=10)
    expires_in = models.IntegerField()
    access_token = models.CharField(max_length=150)
    scope = models.CharField(max_length=150)
    refresh_token = models.CharField(max_length=150)
    expires_at = models.FloatField()

    def get_expire_date(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.expires_at))
    get_expire_date.short_description = "Expire date"


    class Meta:
        verbose_name = "Access Token"
        verbose_name_plural = "Access Tokens"
