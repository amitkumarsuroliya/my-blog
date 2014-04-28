from django.conf import settings
from blog.models import Category


def categories(request):
    return {'categories': Category.objects.all()}


def debug(request):
    return {'DEBUG': settings.DEBUG}