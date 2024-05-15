from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Archaeology, Region, Items, News, Video, Picture
from .serializers import (ArchaeologySerializers, RegionSerializers, ItemsSerializers, NewsSerializers,
                          VideoSerializers, PictureSerializers)


@api_view(['GET'])
def paginated_news_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1
    comments = News.objects.all().order_by("id")
    result_page = paginator.paginate_queryset(comments, request)
    serializer = NewsSerializers(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


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


