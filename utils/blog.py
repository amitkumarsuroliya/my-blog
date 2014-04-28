def is_bot_page_hit(request):
    if 'HTTP_USER_AGENT' in request.META:
        ua = request.META['HTTP_USER_AGENT']
        bot_ua_mark_words = ['inagist.com', 'panscient.com', 'facebookexternalhit', 'ysearch/slurp', 'vkshare',
                             'crawler', 'spider', 'bot', 'java-client', '()', 'feedfetcher', 'snippet']
        if not ua:
            return True

        if any([word in ua.lower() for word in bot_ua_mark_words]):
            return True

    return False