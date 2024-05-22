from rest_framework import serializers
from rest_framework.response import Response

from .models import About, Scientists, ElectronicBooks, Contact, Address

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'description']


class ScientistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientists
        fields = ['id', 'name', 'description']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email', 'description', 'created_at', 'updated_at']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'adres', 'phone', 'email']


class ElectronicBooksSerializer(serializers.ModelSerializer):
    file_books = serializers.SerializerMethodField()

    class Meta:
        model = ElectronicBooks
        fields = ('id', 'name', 'file_books',)

    def get_file_books(self, instance):
        request = self.context.get('request')
        file_books = instance.file_books.all()
        if file_books and hasattr(file_books[0], 'file') and file_books[0].file:  # Fayl mavjudligini tekshirish
            return [{'id': img.id, 'title': img.title, 'file_books': request.build_absolute_uri(img.file.url)} for img
                    in file_books]
        else:
            return None


class ElectronicBooksLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicBooks
        fields = ['id', 'like',]






