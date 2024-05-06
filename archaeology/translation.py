from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import News, NewsVideo, NewsPicture, Video, Picture


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(NewsVideo)
class NewsVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(NewsPicture)
class NewsVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Picture)
class PictureTranslationOptions(TranslationOptions):
    fields = ('title',)