from .models import Entry


def news(request):
    """has_news: whether to link the news section; templates call the method, so it only queries when used."""
    return {'has_news': Entry.objects.current().exists}
