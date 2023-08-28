from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from ckeditor.fields import RichTextField
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False


class User(AbstractUser):
    email = models.EmailField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "The email must be unique"
        }
    )
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_images", storage=MediaStorage()
    )
    followers = models.ManyToManyField("Follow")
    linkedIn_url = models.URLField()
    github_url = models.URLField()
    bio = RichTextField()
    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_profile_picture(self):
        url = ""
        try:
            url = self.profile_image.url
        except:
            url = ""
        return url


class Follow(models.Model):
    followed = models.ForeignKey(
        User,
        related_name='user_followers',
        on_delete=models.CASCADE
    )
    followed_by = models.ForeignKey(
        User,
        related_name='user_follows',
        on_delete=models.CASCADE
    )
    muted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.followed_by.username} started following {self.followed.username}"



