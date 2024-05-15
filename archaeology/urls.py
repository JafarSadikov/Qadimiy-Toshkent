from django.urls import path
from .views import (region_list, region_detail, archaeology_list, archaeology_detail, items_list,
                    items_detail, news_list, news_detail, video_detail, video_list, picture_list, picture_detail,
                    paginated_news_list)


urlpatterns = [
    path('region', region_list),
    path('region/<int:pk>/', region_detail),

    path('archaeology_list/', archaeology_list),
    path('archaeology_detail/<int:pk>/', archaeology_detail),

    path('items_list/',  items_list),
    path('items_detail/<int:pk>/', items_detail),

    path('news_list/', news_list),
    path('news_paginated/', paginated_news_list),
    path('news_detail/<int:pk>/', news_detail),

    path('video_list/', video_list),
    path('video_detail/<int:pk>/', video_detail),

    path('picture_list/', picture_list),
    path('picture_detail/<int:pk>/', picture_detail),

]