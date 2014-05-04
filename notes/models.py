from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
# from social_publisher.mixins import SocialPublisher
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True, default='')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name


class Article(models.Model):
    LANGUAGE_CHOICES = (
        ('en', 'English'),
        ('ru', 'Russian'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    preview_image = ThumbnailerImageField(upload_to='preview', blank=True, null=True, default=None)
    preview = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(null=True, blank=True, default=None)
    author = models.ForeignKey(User, null=True, blank=True, default=None)
    category = models.ForeignKey(Category, null=True, blank=True, default=None)

    # system
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published_at',)


# @receiver(post_save, sender=Article)
# def create_profile(sender, instance, created, **kwargs):
#     """Publish to social networks whenever an object is created."""
    # instance.publish()
    # albums = instance.get_vkontakte_albums()
    # for album in albums:
    #     print album['title'].encode('utf-8').decode('utf-8')

