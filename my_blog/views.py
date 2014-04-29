from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import check_for_language


def about(request):
    return render(request, 'site/about.html', {'active_menu': 'about'})