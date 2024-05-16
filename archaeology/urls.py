from django.urls import path

from .down import File_downloadView, File_download
from .views import (region_list, region_detail, archaeology_list, archaeology_detail, items_list,
                    items_detail, news_list, news_detail, video_detail, video_list, picture_list, picture_detail,
                    ItemsLikeAPIView, paginated_news_list, ArchaeologyLikeAPIView)

urlpatterns = [

    path('region', region_list),
    path('region/<int:pk>/', region_detail),

    path('arxiv/', archaeology_list),
    path('arxiv/<int:pk>/', archaeology_detail),
    path('arxiv/<int:pk>/like', ArchaeologyLikeAPIView.as_view()),
    path('arxiv/downland/<int:pk>/', File_downloadView.as_view()),

    path('items/', items_list),
    path('items/<int:pk>/', items_detail),
    path('items/<int:pk>/like', ItemsLikeAPIView.as_view()),
    path('items/downland/<int:pk>/', File_download.as_view()),

    path('news', news_list),
    path('news/<int:pk>/', news_detail),

    path('video', video_list),
    path('video/<int:pk>/', video_detail),

    path('picture', picture_list),
    path('picture/<int:pk>/', picture_detail),
]
