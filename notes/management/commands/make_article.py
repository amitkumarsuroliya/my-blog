# -*- coding: utf-8 -*-
import re
from BeautifulSoup import BeautifulSoup

from django.core.management.base import BaseCommand, CommandError
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        text_file = open('article.txt', 'r')
        text = text_file.read()
        text_file.close()

        text = text.replace('\n\n', '\n')
        rows = text.split('\n')

        article = ''
        count_paragraphs = 0.0
        for row in rows:
            if 'http' in row:
                article += self.make_image_div(row)
            elif row.endswith('+'):
                article += self.make_header(row)
            else:
                article += self.make_paragraph(row)

            count_paragraphs += 1

            print str(int((count_paragraphs / len(rows)) * 100)) + '%'

        article_file = open('complete_article.txt', 'w')
        article_file.write(article.encode('utf-8'))
        article_file.close()

    def get_image_src(self):
        return self.soup.findAll('div', {'id': 'allsizes-photo'})[0].find('img')['src']

    def make_header(self, text):
        text = text[0:-1]
        return '<h2>%s</h2>\n\n' % text.decode('utf-8')

    def make_paragraph(self, text):
        return '<p>%s</p>\n\n' % text.decode('utf-8')

    def make_image_div(self, url):
        url_array = url.split('/')
        url = 'https://www.flickr.com/photos/nihisil/%s/sizes/l/' % url_array[5]

        r = requests.get(url)
        self.soup = BeautifulSoup(r.text)

        small_image = self.get_image_src()

        big_image_url = 'https://www.flickr.com/photos/nihisil/%s/sizes/k/' % url_array[5]
        r = requests.get(big_image_url)
        self.soup = BeautifulSoup(r.text)
        big_image = self.get_image_src()

        image = """<div class="image_box">
    <a class="fancybox" title="" href="%(big_image)s" rel="group">
        <img src="%(small_image)s" alt="" />
    </a>
</div>\n\n""" % ({'big_image': big_image, 'small_image': small_image})

        return image
