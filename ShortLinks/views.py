from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from ShortLinks.Helpers import Helpers
from ShortLinks.ViewModels.IndexViewModel import IndexViewModel
from ShortLinks.ViewModels.ProfileViewModel import ProfileViewModel
from .models import ShortLink
from ShortLinks.Respositories.ShortLinksRepository import ShortLinksRepository

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class Index(View):
    templateName = 'ShortLinks/Index/index.html'

    def get(self, request):
        lastTenUrls = ShortLink.objects.order_by('CreationDate')\
            .filter(ExpirationDate__gt=timezone.now(), CreatedBy__id=3)[:10]

        model = IndexViewModel
        model.links = lastTenUrls
        model.host = Helpers.getAbsoluteUrl(request)
        if 'error' in request.session:
            model.error = request.session['error']
            request.session['error'] = None
        context = {'model': model}
        return render(request, self.templateName, context)


class RedirectUrl(View):

    def get(self, request, urlId):
        try:
            shortLink = ShortLink.objects.get(ShortLinkId=urlId)
        except ShortLink.DoesNotExist:
            raise Http404('Link does not exist')

        shortLink.TimesUsed += 1
        shortLink.save()
        return HttpResponseRedirect(shortLink.LongLinkValue)


class CreateShortLink(View):
    def post(self, request):
        from ShortLinks.Services.ShortLinksService import ShortLinksService

        longLink = request.POST['LongLinkValue']
        from pytz import utc
        expirationDate = datetime.strptime(request.POST.get('expirationDate', '0001/01/01 00:00'), "%Y/%m/%d %H:%M").astimezone(utc)
        private = request.POST.get('private')

        next = request.POST.get('next', '/')

        try:
            ShortLinksService.createShortLink(longLink, expirationDate, request.user, private)
        except Exception as e:
            request.session['error'] = str(e)
            return redirect(next)

        return redirect(next)


def details(request, urlId):
    shortUrl = ShortLink.objects.get(ShortLinkId=urlId)
    context = {'shortUrl': shortUrl}
    return render(request, 'ShortLinks/details.html', context)


class Profile(LoginRequiredMixin, View):
    print('Admin_View')
    login_url = '/login/'
    templateName = 'ShortLinks/Profile/profile.html'

    def get(self, request):
        links = ShortLinksRepository.getAllLinksFor(request.user)

        model = ProfileViewModel
        model.host = Helpers.getAbsoluteUrl(request)
        model.links = links

        context = {'model': model}
        return render(request, self.templateName, context)

    # def post(self, request):
    #     return redirect('ShortLinks:profile')
