from modeltranslation.translator import TranslationOptions, register
from outher.models import Scientists, ElectronicBooks, Address, About, FileBook


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Scientists)
class ScientistsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(ElectronicBooks)
class ElectronicTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(FileBook)
class FileBookTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('adres',)


