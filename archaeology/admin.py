from django.contrib import admin
from.models import Archaeology, Region, Items, News, Video, Picture, ArchaeologyPicture, ArchaeologyVideo

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


admin.site.register(Archaeology)
admin.site.register(Region)
admin.site.register(Items)
admin.site.register(News)
admin.site.register(Video)
admin.site.register(Picture)
admin.site.register(ArchaeologyPicture)
admin.site.register(ArchaeologyVideo)

from django.contrib import admin

# Register your models here.
