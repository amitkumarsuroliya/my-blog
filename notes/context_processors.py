from django.conf import settings
from notes.models import Category


def categories(request):
    return {'categories': Category.objects.all()}


def debug(request):
    return {'DEBUG': settings.DEBUG}


def settings_variables(request):
    return {
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
        'GOOGLE_ANALYTICS_SITE': settings.GOOGLE_ANALYTICS_SITE,
        'YANDEX_METRIKA_ID': settings.YANDEX_METRIKA_ID,
        'TWITTER_ACCOUNT': settings.TWITTER_ACCOUNT,
        'HYPER_COMMENTS_ID': settings.HYPER_COMMENTS_ID,
    }