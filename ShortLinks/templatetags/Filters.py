from datetime import datetime, timedelta

from django import template
from django.utils import timezone
from pytz import utc

register = template.Library()


@register.filter(name='linkTTLLeft')
def linkTTLLeft(value: datetime):
    '''
    Returns how much time left until some date
    '''
    res = value - timezone.now()
    time1 = timezone.now()
    res = res - timedelta(microseconds=res.microseconds)
    if res < timedelta(hours=0, minutes=0, seconds=0):
        res = 'Expired'
    return res