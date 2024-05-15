from rest_framework import serializers
from archaeology.models import Region, Archaeology, Items, News, Video, Picture


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'title', 'longitude', 'latitude')


class ArchaeologySerializers(serializers.ModelSerializer):
    class Meta:
        model = Archaeology
        fields = ('id', 'title', 'like', 'region', 'password_image', 'create', 'update')


class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'title', 'like', 'password_image', 'create', 'update')


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'title_ru', 'title_en', 'descriptions', 'descriptions_ru', 'descriptions_en', 'create', 'update')


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title')


class PictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'title')
