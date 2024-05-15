from django.urls import path

from .dawload import FileDownload
from .views import about_list, about_detail, scientist_detail, electronic_books_detail, ElectronicListLikeAPIView
from .views import ContactListCreateView, address_list_create, address_edit, ScientistListAPIView, ElectronicListAPIView

urlpatterns = [
    path('about/', about_list),
    path('about/<int:pk>/', about_detail),
    path('scientists/', ScientistListAPIView.as_view(), name='scientist-list'),
    path('scientists/<int:pk>/', scientist_detail),
    path('electronics/', ElectronicListAPIView.as_view(), name='electronics-list'),
    path('electronic_books/<int:pk>/', electronic_books_detail),
    path('electronic_bookslike/<int:pk>/like', ElectronicListLikeAPIView.as_view()),
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('addresses/', address_list_create, name='address-list-create'),
    path('addresses/<int:pk>/', address_edit, name='address-edit'),
    path('file/<int:pk>/', FileDownload.as_view(), name='file_download'),


]






