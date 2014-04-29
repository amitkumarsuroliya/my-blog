from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from notes.models import Article, Category
from utils.blog import is_bot_page_hit


def home(request):
    articles = Article.objects.all()
    return render(request, 'notes/home.html', {'articles': articles})


def view_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    user = request.user
    if not user.is_authenticated() and not is_bot_page_hit(request):
        article.views_count += 1
        article.save()
    relative_articles = Article.objects.filter(category_id=article.category_id).exclude(id=article.id).order_by('?')[:5]
    return render(request, 'notes/view_article.html', {'article': article, 'relative_articles': relative_articles})


def by_category(request, category):
    category = get_object_or_404(Category, slug=category)
    ancestors = category.get_ancestors(include_self=True)
    categories = [c.id for c in category.get_descendants(True)]
    articles = Article.objects.filter(category__in=categories)
    return render(request, 'notes/category.html',
                  {'articles': articles, 'category': category, 'ancestors': ancestors})
