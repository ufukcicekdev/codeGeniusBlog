"""blog_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.upload_img_file import upload_blog_image,upload_blog_file
from blog_website.ckeditor_views import editorjs_file_upload,editorjs_image_upload
from blog_website.ckeditor_views import editorjs_file_upload,editorjs_image_upload
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('user_profile.urls')),

    
    path('update_blog/<str:slug>/uploadi/', upload_blog_image, name='upload_blog_image'),
    path('update_blog/<str:slug>/uploadf/', upload_blog_file, name='upload_blog_file'),
    path('add_blog/uploadi/',   editorjs_image_upload, name='editorjs_image_upload'),
    path('add_blog/uploadf/',   editorjs_file_upload, name='editorjs_file_upload'),

          
    path('profile/uploadi/',    editorjs_image_upload, name='editorjs_image_upload'),
    path('profile/uploadf/',    editorjs_file_upload, name='editorjs_file_upload'),

] 



