from datetime import timedelta, datetime

import shortuuid
from django.contrib.auth.models import User
from django.utils import timezone

from ShortLinks.Respositories.ShortLinksRepository import ShortLinksRepository
from ShortLinks.Services.validateLinkCreation import LinkValidationService
from ShortLinks.models import ShortLink


class ShortLinksService:
    @staticmethod
    def createShortLink(long: str, expirationDate: datetime, user: User, private: bool):

        if not private:
            userToSave = User.objects.get(id=3)
        else:
            userToSave = user

        if not LinkValidationService.linkIsValid(long):
            raise ValueError('Invalid link')
        if not LinkValidationService.linkContainsHttp(long):
            long = 'http://' + long

        if LinkValidationService.expirationDateIsValid(expirationDate):
            raise ValueError('Invalid expiration date')

        shortLink = shortuuid.ShortUUID().random(length=5)
        shortLink = ShortLink(
            ShortLinkId=shortLink,
            LongLinkValue=long,
            CreationDate=timezone.now(),
            ExpirationDate=expirationDate,
            CreatedBy=userToSave)

        ShortLinksRepository.addShortLink(shortLink)

    @staticmethod
    def getAvailableLinksThatExpireBy(finalDate: datetime, user: User):
        # date = timezone.now() + timedelta(hours=hours)
        links = ShortLinksRepository.getAvailableActiveLinksFor(user).filter(ExpirationDate__lt=finalDate)
        return links
