import re
from datetime import datetime

from django.utils import timezone

LinkRegEx = r"[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
ContainsHttpRegEx = r"^.*https?://"

from LinkShortener.globalVariables import *


class LinkValidationService:

    @staticmethod
    def linkDataValid(link, ttl):
        ttlValid = LinkValidationService.expirationDateIsValid(ttl)
        linkValid = LinkValidationService.linkIsValid(link)

    @staticmethod
    def expirationDateIsValid(expidrationDate: datetime):
        return expidrationDate < timezone.now()

    @staticmethod
    def linkIsValid(link: str):
        pattern = re.compile(LinkRegEx)
        return bool(re.search(pattern, link))

    @staticmethod
    def linkContainsHttp(link: str):
        pattern = re.compile(ContainsHttpRegEx)
        return  bool(re.search(pattern, link))
