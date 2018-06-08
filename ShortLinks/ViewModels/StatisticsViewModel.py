from datetime import datetime

from ShortLinks.models import ShortLink


class StatisticsViewModel:
    links: ShortLink
    totalShortLinksCount: int
    currentlyActiveLinksCount: int
    host: str
    filter: datetime
    error: str
