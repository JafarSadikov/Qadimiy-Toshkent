from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework.generics import RetrieveUpdateAPIView
from .models import Archaeology, Region, Items, News, Video, Picture
from .serializers import (ArchaeologySerializers, RegionSerializers, ItemsSerializers, NewsSerializers,
                          VideoSerializers, PictureSerializers, ArchaeologyLikeSerializer, ItemsLikeSerializer)

from django.shortcuts import get_object_or_404
from rest_framework import status
from .filters import CategoryFilter


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
def archaeology_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    comments = Archaeology.objects.all().order_by("id")
    user_filter = CategoryFilter(request.GET, queryset=comments)
    result_page = paginator.paginate_queryset(user_filter.qs, request)
    serializer = ArchaeologySerializers(result_page, many=True, context={'request': request})
    serializer_url = serializer.data
    for obj_url in serializer_url:
        if obj_url.get('password_image'):
            obj_url['password_image'] = request.build_absolute_uri(obj_url['password_image'])
    return paginator.get_paginated_response(serializer_url)


@api_view(['GET'])
def archaeology_detail(request, pk):
    try:
        archaeology = Archaeology.objects.get(pk=pk)
    except Archaeology.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    archaeology.view_count += 1
    archaeology.save()

    serializer = ArchaeologySerializers(archaeology, context={'request': request})
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
def items_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1
    comments = Items.objects.all().order_by("id")
    user_filter = CategoryFilter(request.GET, queryset=comments)
    result_page = paginator.paginate_queryset(user_filter.qs, request)
    serializer = ItemsSerializers(result_page, many=True, context={'request': request})
    serializer_url = serializer.data
    for obj_url in serializer_url:
        if obj_url.get('password_image'):
            obj_url['password_image'] = request.build_absolute_uri(obj_url['password_image'])
    return paginator.get_paginated_response(serializer_url)


@api_view(['GET'])
def items_detail(request, pk):
    try:
        items = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    items.view_count += 1
    items.save()

    serializer = ItemsSerializers(items, context={'request': request})
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
