from django.contrib import admin
from .models import ElectronicBooks, About, Scientists, Address, FileBook


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldset = ('title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en',)


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldset = ('name_uz', 'name_ru', 'name_en', 'description_uz', 'description_ru', 'description_en',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('adres',)
    fieldset = ('adres_uz', 'adres_ru', 'adres_en',)


class FileBookInline(admin.TabularInline):
    model = FileBook


@admin.register(ElectronicBooks)
class ElectronicAdmin(admin.ModelAdmin):
    inlines = (FileBookInline, )
    list_display = ('name',)
    fieldset = ('name_uz', 'name_ru', 'name_en',)

class FileBookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'file', 'downloads')
    fields = ('title_uz', 'title_ru', 'title_en', 'author', 'file',)


admin.site.register(FileBook, FileBookAdmin)

