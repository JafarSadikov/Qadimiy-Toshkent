from django.contrib import admin

from .models import Archaeology, Region, Items, News, Video, Picture, ArchaeologyPicture, ArchaeologyVideo, \
    NewsVideo, NewsPicture, SubVideo, SubPicture, ItemsVideo, ItemsPicture


class NewsVideoTabularInline(admin.TabularInline):
    model = NewsVideo
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'video']


class NewsPictureTabularInline(admin.TabularInline):
    model = NewsPicture
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'image']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'context',)
    inlines = [NewsVideoTabularInline, NewsPictureTabularInline]
    fields = ['title_uz', 'title_en', 'title_ru', 'context_uz', 'context_en', 'context_ru']


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


class Archaeology_Video(admin.TabularInline):
    model = ArchaeologyVideo
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'video']


class Archaeology_Picture(admin.TabularInline):
    model = ArchaeologyPicture
    fields = ['title_uz', 'title_ru', 'title_en', 'link', 'image']


@admin.register(Archaeology)
class ArchaeologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'context',)
    inlines = [Archaeology_Video, Archaeology_Picture]
    fields = ('context_uz', 'context_en', 'context_ru', 'title_uz', 'title_ru', 'title_en', 'password_image', 'region')


class SubVideoTabularInline(admin.TabularInline):
    model = SubVideo
    fields = ['videos', 'link', 'video']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SubVideoTabularInline]
    fields = ('title_uz', 'title_ru', 'title_en')


class SubPictureTabularInline(admin.TabularInline):
    model = SubPicture
    fields = ['picture', 'link', 'image']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SubPictureTabularInline]
    fields = ('title_uz', 'title_ru', 'title_en')


admin.site.register(Region)

