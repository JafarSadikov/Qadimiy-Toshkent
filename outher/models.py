from django.db import models

from users.models import CustomUser


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class AboutImage(models.Model):
    file = models.FileField(upload_to='images/', blank=True, null=True)
    about = models.ForeignKey(About, on_delete=models.CASCADE)


class Scientists(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)


class ScientistsImage(models.Model):
    file = models.FileField(upload_to='images/', blank=True, null=True)
    scientists = models.ForeignKey(Scientists, on_delete=models.CASCADE)


class ElectronicBooks(models.Model):
    name = models.CharField(max_length=150)
    like = models.IntegerField(default=0, blank=True, null=True)
    liked_users = models.ManyToManyField(CustomUser, related_name='liked_books', blank=True)

    def __str__(self):
        return self.name


class FileBook(models.Model):
    file = models.FileField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    downloads = models.IntegerField(default=0, blank=True, null=True)
    author = models.ForeignKey(ElectronicBooks, on_delete=models.CASCADE, related_name='file_books')


class Contact(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Address(models.Model):
    adres = models.CharField(max_length=200)
    phone = models.CharField(max_length=17)
    email = models.EmailField()
