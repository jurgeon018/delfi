from django.contrib.sitemaps import Sitemap 
from core.models import *
from django.urls import reverse  

class PostSitemap(Sitemap):
    i18n = True 
    def items(self):
        return Post.objects.all()


class StaticViewSitemap(Sitemap):
    i18n = True 
    def items(self):
        return [
            'index', 
            'blog',
            'contact_us',
            'park',
            'order',
            'about_us',
            'thank_you'
        ]
    def location(self, item):
        return reverse(item)

