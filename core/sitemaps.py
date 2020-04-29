from django.contrib.sitemaps import Sitemap 
from core.models import *
from django.urls import reverse  




class PostSitemap(Sitemap):
    i18n = True 
    changefreq = 'weekly' 
    protocol = 'https'
    priority = 1

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
            return obj.updated



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




