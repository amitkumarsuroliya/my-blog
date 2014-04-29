from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from notes.models import Article, Category


class ArticleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.published_at

    def location(self, obj):
        return reverse('view_article', kwargs={'slug': obj.slug})


class CategorySitemap(Sitemap):
    changefreq = 'daily'
    priority = 1

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('by_category', kwargs={'category': obj.slug})


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['home', 'about']

    def location(self, item):
        return reverse(item)