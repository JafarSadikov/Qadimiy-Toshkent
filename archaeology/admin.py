from django.contrib import admin
from .models import Archaeology, Region, Items, News, Video, Picture, ArchaeologyPicture, ArchaeologyVideo, ItemsVideo, \
    ItemsPicture


class Archaeology_Video(admin.TabularInline):
    model = ArchaeologyVideo


class archaeology_Picture(admin.TabularInline):
    model = ArchaeologyPicture


class archaeologyAdmin(admin.ModelAdmin):
    inlines = [archaeology_Picture, Archaeology_Video]

    class Meta:
        model = Archaeology


class items_Video(admin.TabularInline):
    model = ItemsVideo


class items_Picture(admin.TabularInline):
    model = ItemsPicture


class itemsAdmin(admin.ModelAdmin):
    inlines = [items_Video, items_Picture]

    class Meta:
        model = Items


admin.site.register(Archaeology, archaeologyAdmin)
admin.site.register(Region)
admin.site.register(Items, itemsAdmin)
admin.site.register(News)
admin.site.register(Video)
admin.site.register(Picture)
