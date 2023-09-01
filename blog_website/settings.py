"""
Django settings for blog_website project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["codegenius.blog"]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://*.codegenius.blog"]
# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'blog',
    'user_profile',
    'notification',
    'django_editorjs'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout'
]

ROOT_URLCONF = 'blog_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.get_all_categories',
                'user_profile.context_processors.user_notifications'
            ],
        },
    },
]

WSGI_APPLICATION = 'blog_website.wsgi.application'

ROBOTS_TXT_PATH = os.path.join(BASE_DIR, 'robots.txt')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
        'OPTIONS': {
            'sslmode': 'require',  # SSL gereklilik durumu
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,"media")

STATIC_URL = '/static/'
STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static_files')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user_profile.User'

AUTHENTICATION_BACKENDS = (
    "user_profile.backends.EmailAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend"
)

AUTO_LOGOUT = {'IDLE_TIME': 21600}  # logout after 10 minutes of downtime


SESSION_TIMEOUT_REDIRECT = 'home'

# CKEDITOR_UPLOAD_PATH = "uploads/"
#CKEDITOR_STORAGE_BACKEND = 'django.core.files.storage.FileSystemStorage'
#FILEBROWSER_REMOVE_DIALOG_TABS = 'image:Upload'
# CKEDITOR_IMAGE_BACKEND = "pillow"
# CKEDITOR_UPLOAD_SLUGIFY_FILENAME =False

# CKEDITOR_CONFIGS = {
#    'default': {
#         'filebrowserUploadUrl': '/ckeditor/upload/',
#         'filebrowserBrowseUrl': '/ckeditor/browse/',
#         'toolbar': 'Full',  # Toolbar ayarları düzeltildi
#         'toolbar_Full': [
#             ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
#             ['Link', 'Unlink', 'Anchor'],
#             ['Image', 'Flash', 'Table', 'HorizontalRule'],
#             ['TextColor', 'BGColor'],
#             ['Smiley', 'SpecialChar'], ['Source'],
#             ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
#             ['NumberedList', 'BulletedList'],
#             ['Indent', 'Outdent'],
#             ['Maximize'],
#             {'name': 'about', 'items': ['CodeSnippet']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#         ],
#         'tabSpaces': 4,
#         'fillEmptyBlocks': False,
#         'extraPlugins': 'justify,liststyle,indent,codesnippet,devtools,uploadimage',  # Resim eklentisi eklendi
#         #'uploadUrl': '/ckeditor/upload/',  # Resim yükleme URL'si eklendi
#    },
# }


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')
AWS_DEFAULT_ACL = os.getenv('AWS_DEFAULT_ACL')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
