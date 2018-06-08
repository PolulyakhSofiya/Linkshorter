from django.contrib.auth.models import User
from django.utils import timezone

from ShortLinks.models import ShortLink


class ShortLinksRepository:

    @staticmethod
    def getAllLinks():
        links = ShortLink.objects.all()
        return links

    @staticmethod
    def addShortLink(shortLink: ShortLink):
        if shortLink is None:
            return
        shortLink.save()

    @staticmethod
    def getAllLinksFor(user: User):
        links = ShortLink.objects.filter(CreatedBy=user)
        return links

    @staticmethod
    def getPublicAndPrivateLinksFor(user: User):
        links = ShortLink.objects.filter(CreatedBy_id__in=[user.id, 3])
        return links

    @staticmethod
    def getAllActiveLinks():
        links = ShortLink.objects.filter(ExpirationDate__gt=timezone.now())
        return links

    @staticmethod
    def getAvailableActiveLinksFor(user: User):
        links = ShortLinksRepository.getAllActiveLinks().filter(CreatedBy_id__in=[user.id, 3])
        return links
