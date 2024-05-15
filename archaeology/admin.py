from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register,TranslationOptions

from .models import Archaeology, Region, Items, News, Video, Picture, ArchaeologyPicture, ArchaeologyVideo, ItemsVideo,\
    ItemsPicture


class items_Video(admin.TabularInline):
    model = ItemsVideo
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'video']


class items_Picture(admin.TabularInline):
    model = ItemsPicture
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'image']


@admin.register(Items)
class itemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'context',)
    inlines = [items_Video, items_Picture]
    fields = ('context_uz', 'context_en', 'context_ru', 'title_uz', 'title_ru', 'title_en', 'password_image',
               )


class ArchaeologyVideoInline(admin.TabularInline):
    model = ArchaeologyVideo
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'video']


class ArchaeologyPictureInline(admin.TabularInline):
    model = ArchaeologyPicture
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'image']


@admin.register(Archaeology)
class ArchaeologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'context',)
    inlines = [ArchaeologyPictureInline, ArchaeologyVideoInline]
    fields = ('context_uz', 'context_en', 'context_ru', 'title_uz', 'title_ru', 'title_en', 'password_image', 'region')


admin.site.register(Region)
admin.site.register(News)
admin.site.register(Video)
admin.site.register(Picture)
