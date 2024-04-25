from django.db import models
import time
import pytz
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import make_aware


class Access_token(models.Model):
    token_type = models.CharField(max_length=10)
    expires_in = models.IntegerField()
    access_token = models.CharField(max_length=150)
    scope = models.CharField(max_length=150)
    refresh_token = models.CharField(max_length=150)
    expires_at = models.FloatField()

    def get_expire_date(self):
        return make_aware(datetime.fromtimestamp(time.mktime(time.localtime(self.expires_at))), pytz.timezone('Europe/Madrid'))
    get_expire_date.short_description = "Expire date"

    def is_valid(self):
        if self.get_expire_date() > timezone.now():
            return True
        return False
    is_valid.short_description = "Valid"
    is_valid.boolean = True



    class Meta:
        verbose_name = "Access Token"
        verbose_name_plural = "Access Tokens"
