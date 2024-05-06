from django.contrib import admin
from modeltranslation.translator import TranslationOptions

from .models import Archaeology, Region, Items, News, Video, Picture, ArchaeologyPicture, ArchaeologyVideo, \
    NewsVideo, NewsPicture, SubVideo, SubPicture

#
# class Archaeology_Video(admin.TabularInline):
#     models = ArchaeologyVideo
#
#
# class archaeology_Picture(admin.TabularInline):
#     models = ArchaeologyPicture
#
#
# class archaeologyAdmin(admin.ModelAdmin):
#     inlines = [archaeology_Picture, Archaeology_Video]


class NewsVideoTabularInline(admin.TabularInline):
    model = NewsVideo


class NewsPictureTabularInline(admin.TabularInline):
    model = NewsPicture


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsVideoTabularInline, NewsPictureTabularInline]

    class Meta:
        model = News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


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


admin.site.register(Archaeology)
admin.site.register(Region)
admin.site.register(Items)
admin.site.register(News, NewsAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(ArchaeologyPicture)
admin.site.register(ArchaeologyVideo)


