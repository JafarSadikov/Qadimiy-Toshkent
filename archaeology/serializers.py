from rest_framework import serializers
from archaeology.models import Region, Archaeology, Items, News, Video, Picture


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'title', 'longitude', 'latitude')


class ArchaeologySerializers(serializers.ModelSerializer):
    class Meta:
        model = Archaeology
        fields = ['id', 'title', 'context', 'region', 'downloads', 'password_image', 'view_count', 'create', 'update']


class ArchaeologyLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archaeology
        fields = ['id', 'like', ]


class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'title', 'context', 'downloads', 'view_count', 'password_image', 'create', 'update')


class ItemsLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'like', ]


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'context', 'create', 'update')


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title')


class PictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'title')
