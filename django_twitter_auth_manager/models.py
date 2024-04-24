from django.db import models
import time
import pytz
from datetime import datetime
from time import mktime
from django.utils.timezone import make_aware

class Access_token(models.Model):
    token_type = models.CharField(max_length=10)
    expires_in = models.IntegerField()
    access_token = models.CharField(max_length=150)
    scope = models.CharField(max_length=150)
    refresh_token = models.CharField(max_length=150)
    expires_at = models.FloatField()

    def get_expire_date(self):
        return make_aware(datetime.fromtimestamp(mktime(time.gmtime(self.expires_at))), timezone=pytz.timezone("Europe/Madrid"))
    get_expire_date.short_description = "Expire date"


    class Meta:
        verbose_name = "Access Token"
        verbose_name_plural = "Access Tokens"
