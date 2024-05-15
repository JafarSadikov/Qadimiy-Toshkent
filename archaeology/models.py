from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
User = get_user_model()


class Region(models.Model):
    title = models.CharField(max_length=60)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.title or ''


class Archaeology(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    context = RichTextField(blank=True, null=True)
    like = models.IntegerField(default=0, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region')
    password_image = models.FileField(upload_to='image', blank=True, null=True)
    downloads = models.IntegerField(default=0, blank=True, null=True)
    users = models.ManyToManyField(User, related_name='liked_kanferensiyalar', blank=True)
    view_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Archaeology'
        verbose_name_plural = 'Archaeologys'

    def __str__(self):
        return self.title or ''


class ArchaeologyVideo(models.Model):
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    title = models.CharField(max_length=60)
    name = models.ForeignKey(Archaeology, on_delete=models.CASCADE, related_name='archaeologyVideo')


class ArchaeologyPicture(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(verbose_name='link', blank=True, null=True)
    title = models.CharField(max_length=60)
    name = models.ForeignKey(Archaeology, on_delete=models.CASCADE, related_name='archaeologyPicture')


class Items(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    like = models.IntegerField(default=0, blank=True, null=True)
    users = models.ManyToManyField(User, related_name='like_kanferensiyalar', blank=True)
    password_image = models.FileField(upload_to='images', blank=True, null=True)
    downloads = models.IntegerField(default=0, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title or ''


class ItemsVideo(models.Model):
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    title = models.CharField(max_length=60)
    items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='picture_items')


class ItemsPicture(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(verbose_name='link', blank=True, null=True)
    title = models.CharField(max_length=60)
    items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='video_items')


class News(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title or ''


class NewsVideo(models.Model):
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    title = models.CharField(max_length=60)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_video')


class NewsPicture(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(verbose_name='link', blank=True, null=True)
    title = models.CharField(max_length=60)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_picture')


class Video(models.Model):
    title = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title or ''


class SubVideo(models.Model):
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    videos = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_sub')


class Picture(models.Model):
    title = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        return self.title or ''


class SubPicture(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(verbose_name='link', blank=True, null=True)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='picture_sub')
