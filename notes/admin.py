from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from notes.models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'views_count', 'category')
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = ('http://tinymce.cachefly.net/4.0/tinymce.min.js', 'js/admin.js')


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
