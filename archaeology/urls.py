from django.contrib import admin
from django.urls import path
from .views import (region_list, region_detail, archaeology_list, archaeology_detail, items_list,
                    items_detail, news_list, news_detail, video_detail, video_list, picture_list, picture_detail)

urlpatterns = [
    path('region', region_list),
    path('region/<int:pk>/', region_detail),

    path('arxiv', archaeology_list),
    path('arxiv/<int:pk>/', archaeology_detail),

    path('arxiv',  items_list),
    path('arxiv/<int:pk>/', items_detail),

    path('arxiv', news_list),
    path('arxiv/<int:pk>/', news_detail),

    path('arxiv', video_list),
    path('arxiv/<int:pk>/', video_detail),

    path('arxiv', picture_list),
    path('arxiv/<int:pk>/', picture_detail),

]