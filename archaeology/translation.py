from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import News, NewsVideo, NewsPicture, Video, Picture
from archaeology.models import Archaeology, ArchaeologyVideo, ArchaeologyPicture, Items, ItemsPicture, ItemsVideo


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'context',)


@register(NewsVideo)
class NewsVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(NewsPicture)
class NewsPictureTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Picture)
class PictureTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Archaeology)
class ArchaeologyTranslationOptions(TranslationOptions):
    fields = ('title','context', )


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
