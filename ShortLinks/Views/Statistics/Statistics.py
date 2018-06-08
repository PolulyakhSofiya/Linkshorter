from django.db import IntegrityError
from django.utils import timezone
from django.views import View
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from pytz import utc

from ShortLinks.Helpers import Helpers
from ShortLinks.Respositories.ShortLinksRepository import ShortLinksRepository
from ShortLinks.Services.ShortLinksService import ShortLinksService
from ShortLinks.ViewModels.StatisticsViewModel import StatisticsViewModel


class Statistics(View):
    print('Statistics_View')
    templateName = 'ShortLinks/Statistics/Statistics.html'

    def get(self, request, hours: int = 0):
        links = ShortLinksRepository.getPublicAndPrivateLinksFor(request.user).order_by('-CreatedBy_id', 'ExpirationDate')

        model = StatisticsViewModel
        model.host = Helpers.getAbsoluteUrl(request)
        model.links = links
        model.currentlyActiveLinksCount = ShortLinksRepository.getAllActiveLinks().count()
        model.totalShortLinksCount = ShortLinksRepository.getAllLinks().count()

        context = {'model': model}
        return render(request, self.templateName, context)

    def post(self, request):
        finalDate = datetime.strptime(request.POST.get('finalDate', '0001/01/01 00:00'), "%Y/%m/%d %H:%M")
        print('final: ', finalDate.replace(tzinfo=utc))
        print('now: ', timezone.now().replace(tzinfo=utc))
        model = self.createModel(request)

        if finalDate < datetime.now():
            links = ShortLinksRepository.getPublicAndPrivateLinksFor(request.user).order_by('-CreatedBy_id',
                                                                                            'ExpirationDate')
            model.error = 'Something went wrong, please try again.'
        else:
            links = ShortLinksService.getAvailableLinksThatExpireBy(finalDate, request.user)

        model.links = links
        context = {'model': model}
        return render(request, self.templateName, context)

    @staticmethod
    def createModel(request):
        model = StatisticsViewModel
        model.host = Helpers.getAbsoluteUrl(request)
        model.totalShortLinksCount = ShortLinksRepository.getAllLinks().count()
        model.currentlyActiveLinksCount = ShortLinksRepository.getAllActiveLinks().count()
        return model
