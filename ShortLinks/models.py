from django.contrib.auth.models import User, AnonymousUser
from django.db import models
from django.utils import timezone

from LinkShortener.globalVariables import *

# Create your models here.


class ShortLink(models.Model):
    ShortLinkId = models.CharField(max_length=200)
    LongLinkValue = models.CharField(max_length=5000)
    CreationDate = models.DateTimeField('Creation Date')
    ExpirationDate = models.DateTimeField('Expiration Date', default=timezone.now)
    TimesUsed = models.BigIntegerField(default=0)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE, default=3)

    def __str__(self):
        return '{0} : {1} : {2}'.format(self.ShortLinkId, self.LongLinkValue, self.CreatedBy_id)

    class Meta:
        ordering = ['-CreationDate']
