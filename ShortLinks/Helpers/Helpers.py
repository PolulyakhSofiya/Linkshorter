def absolute(request):
    urls = {
        'ABSOLUTE_ROOT': request.build_absolute_uri('/')[:-1].strip("/"),
        'ABSOLUTE_ROOT_URL': request.build_absolute_uri('/').strip("/"),
        'FULL_URL': request.build_absolute_uri('?')
    }
    return urls


def getAbsoluteUrl(request):
    return absolute(request)['ABSOLUTE_ROOT_URL']
