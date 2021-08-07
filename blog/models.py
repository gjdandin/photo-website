from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse
#from django_resized import ResizedImageField
import datetime

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
#     name = models.CharField(max_length=50, null=True)
#     phone = models.CharField(max_length=50, null=True)
#     email = models.CharField(max_length=50, null=True)
#     profile_pic = models.ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name



class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True, blank=True)


    class Meta: #Order on primary key
        ordering = ['pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname=image_view, kwargs={'pk':self.pk})

    def show_images(self):
        return self.image.image


class Image(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, default='Unsorted')

    title = models.CharField(max_length = 128)
    body = models.TextField(max_length=400, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    thumb_image = ImageSpecField(source='image', processors=[ResizeToFill(750, 500)], format='JPEG', options={'quality':70})
    created_at = models.DateTimeField(auto_now=True)
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    #

    class Meta: #Order on primary key
        ordering = ['pk']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(kwargs={'pk':self.pk})

# class Picture(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.SET_NULL, default=None, null=True, blank=True)
#     name = Post.title
#     image = models.ImageField(null=True, blank=True)


    # def __str__(self):
    #     return self.name