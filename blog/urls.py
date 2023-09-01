from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import CategoryLinkSiteMap,TagsLinkSiteMap
from django.conf.urls import handler404, handler500
from django.views.generic import TemplateView
from .views import *

sitemaps = {
    'categoryLinkSiteMap':CategoryLinkSiteMap, 
    'tagLinkSiteMap':TagsLinkSiteMap
}


urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blogs, name='blogs'),
    path('category_blogs/<str:slug>/', category_blogs, name='category_blogs'),
    path('tag_blogs/<str:slug>/', tag_blogs, name='tag_blogs'),
    path('blog/<str:slug>/', blog_details, name='blog_details'),
    path('add_reply/<int:blog_id>/<int:comment_id>/', add_reply, name='add_reply'),
    path('like_blog/<int:pk>/', like_blog, name='like_blog'),
    path('search_blogs/', search_blogs, name='search_blogs'),
    path('my_blogs/', my_blogs, name='my_blogs'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<str:slug>/', update_blog, name='update_blog'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

]
handler404 = 'blog.views.custom_404_view'
handler500 = 'blog.views.custom_500_view'
