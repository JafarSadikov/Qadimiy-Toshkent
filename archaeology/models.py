from django.db import models


# from ckeditor.fields import RichTextField


class Region(models.Model):
    title = models.CharField(max_length=60)
    longitude = models.FloatField()
    latitude = models.FloatField()


class Archaeology(models.Model):
    title = models.CharField(max_length=60)
    # ckeditor = RichTextField()
    like = models.IntegerField(default=0, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region')
    password_image = models.FileField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


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
    # ckeditor = RichTextField()
    like = models.IntegerField(default=0, blank=True, null=True)
    password_image = models.FileField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


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
    descriptions = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


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


class SubVideo(models.Model):
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    videos = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_sub')


class Picture(models.Model):
    title = models.CharField(max_length=60)


class SubPicture(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(verbose_name='link', blank=True, null=True)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='picture_sub')
