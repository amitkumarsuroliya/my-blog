from django.shortcuts import render


def about(request):
    return render(request, 'my_blog/about.html', {'active_menu': 'about'})