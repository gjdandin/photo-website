from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Picture)
#admin.site.register(Profile)
admin.site.register(Image)

class ImagesInline(admin.TabularInline):
    model = Image

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ['title']

admin.site.register(Album, AlbumAdmin)