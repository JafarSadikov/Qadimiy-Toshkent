from modeltranslation.translator import TranslationOptions, register
from archaeology.models import Archaeology, ArchaeologyVideo, ArchaeologyPicture, Items, ItemsPicture, ItemsVideo


@register(Archaeology)
class ArchaeologyTranslationOptions(TranslationOptions):
    fields = ('title', 'context',)


@register(ArchaeologyVideo)
class ArchaeologyVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ArchaeologyPicture)
class ArchaeologyPictureTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Items)
class ItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'context',)


@register(ItemsVideo)
class ItemsVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ItemsPicture)
class ItemsPictureTranslationOptions(TranslationOptions):
    fields = ('title',)
