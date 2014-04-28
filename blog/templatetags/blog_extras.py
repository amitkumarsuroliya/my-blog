from django import template

register = template.Library()


@register.filter
def social_share_image(article, request):
    image = article.preview_image
    if 'HTTP_USER_AGENT' in request.META:
        ua = request.META['HTTP_USER_AGENT']
        if ua and 'vk.com' in ua:
            image = article.preview_image_small
    return image