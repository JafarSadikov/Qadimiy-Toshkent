from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Archaeology, Region, Items, News, Video, Picture
from .serializers import (ArchaeologySerializers, RegionSerializers, ItemsSerializers, NewsSerializers,
                          VideoSerializers, PictureSerializers, ArchaeologyLikeSerializer, ItemsLikeSerializer)
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def archaeology_list(request):
    comments = Archaeology.objects.all().order_by("id")
    serializer = ArchaeologySerializers(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def archaeology_detail(request, pk):
    try:
        comment = Archaeology.objects.get(pk=pk)
    except Archaeology.DoesNotExist:
        raise Http404

    serializer = ArchaeologySerializers(comment)
    return Response(serializer.data)


class ArchaeologyLikeAPIView(RetrieveUpdateAPIView):
    queryset = Archaeology.objects.all()
    serializer_class = ArchaeologyLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.users.filter(id=user.id).exists()
            if not existing_like:
                instance.users.add(user)
                instance.like += 1
            else:
                instance.users.remove(user)
                instance.like -= 1
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
            pk = self.kwargs.get('pk')
            return get_object_or_404(Archaeology, pk=pk)


@api_view(['GET'])
def region_list(request):
    comments = Region.objects.all().order_by("id")
    serializer = RegionSerializers(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def region_detail(request, pk):
    try:
        comment = Region.objects.get(pk=pk)
    except Archaeology.DoesNotExist:
        raise Http404

    serializer = RegionSerializers(comment)
    return Response(serializer.data)


@api_view(['GET'])
def items_list(request):
    comments = Items.objects.all().order_by("id")
    serializer = ItemsSerializers(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def items_detail(request, pk):
    try:
        comment = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        raise Http404

    serializer = ItemsSerializers(comment)
    return Response(serializer.data)


class ItemsLikeAPIView(RetrieveUpdateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.users.filter(id=user.id).exists()
            if not existing_like:
                instance.users.add(user)
                instance.like += 1
            else:
                instance.users.remove(user)
                instance.like -= 1
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
            pk = self.kwargs.get('pk')
            return get_object_or_404(Items, pk=pk)


@api_view(['GET'])
def news_list(request):
    comments = News.objects.all().order_by("id")
    serializer = NewsSerializers(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news_detail(request, pk):
    try:
        comment = News.objects.get(pk=pk)
    except News.DoesNotExist:
        raise Http404

    serializer = NewsSerializers(comment)
    return Response(serializer.data)


@api_view(['GET'])
def video_list(request):
    comments = Video.objects.all().order_by("id")
    serializer = VideoSerializers(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def video_detail(request, pk):
    try:
        comment = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        raise Http404

    serializer = VideoSerializers(comment)
    return Response(serializer.data)


@api_view(['GET'])
def picture_list(request):
    comments = Picture.objects.all().order_by("id")
    serializer = PictureSerializers(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def picture_detail(request, pk):
    try:
        comment = Picture.objects.get(pk=pk)
    except Picture.DoesNotExist:
        raise Http404

    serializer = PictureSerializers(comment)
    return Response(serializer.data)


