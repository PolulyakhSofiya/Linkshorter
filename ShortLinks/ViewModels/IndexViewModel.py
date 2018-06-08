from datetime import timedelta

from ShortLinks.models import ShortLink


class IndexViewModel:
    links: ShortLink
    error: str
    host: str
    linkTimeleft: timedelta