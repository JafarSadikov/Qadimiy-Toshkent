from django.contrib import admin
from modeltranslation.translator import TranslationOptions

from .models import Archaeology, Region, Items, News, Video, Picture, ArchaeologyPicture, ArchaeologyVideo, \
    NewsVideo, NewsPicture, SubVideo, SubPicture, ItemsVideo, ItemsPicture


class NewsVideoTabularInline(admin.TabularInline):
    model = NewsVideo


class NewsPictureTabularInline(admin.TabularInline):
    model = NewsPicture


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsVideoTabularInline, NewsPictureTabularInline]
    fields = ['title_en', 'title_ru', 'context_en', 'context_ru']

    class Meta:
        model = News


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
    fields = ('context_uz', 'context_en', 'context_ru', 'title_uz', 'title_ru', 'title_en', 'password_image',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'context')


class NewsVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


class NewsPictureTranslationOptions(TranslationOptions):
    fields = ('title',)


class SubVideoTabularInline(admin.TabularInline):
    model = SubVideo


class VideoAdmin(admin.ModelAdmin):
    inlines = [SubVideoTabularInline]

    class Meta:
        model = Video


class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


class SubPictureTabularInline(admin.TabularInline):
    model = SubPicture


class PictureAdmin(admin.ModelAdmin):
    inlines = [SubPictureTabularInline]

    class Meta:
        model = Picture


class PictureTranslationOptions(TranslationOptions):
    fields = ('title',)


admin.site.register(Region)
admin.site.register(News, NewsAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(ArchaeologyPicture)
admin.site.register(ArchaeologyVideo)


