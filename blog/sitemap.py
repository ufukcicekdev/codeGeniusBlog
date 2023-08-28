from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from blog.models import *
from user_profile.models import models
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

startdate = datetime.today()
enddate = startdate + relativedelta(years=10)



class CategoryLinkSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def location(self,obj):
        return f"/category/{obj.slug}"
    
class TagsLinkSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Tag.objects.all()

    def location(self,obj):
        return f"/tag_blogs/{obj.slug}"
    
