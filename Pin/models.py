from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models import signals
from storages.backends.dropbox import DropBoxStorage
from django.core.validators import validate_image_file_extension as vife
from django.dispatch import receiver


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    danger = models.CharField(max_length=50, verbose_name='Опасность')
    image = models.ImageField(upload_to='category', storage=DropBoxStorage(), null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Images(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название картинки")
    img = models.ImageField(upload_to='img', storage=DropBoxStorage(), null=True, blank=True)


class Pin(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    lat = models.DecimalField(max_digits=14, decimal_places=12, verbose_name='Широта')
    lng = models.DecimalField(max_digits=14, decimal_places=12, verbose_name='Долгота')
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.PROTECT, verbose_name='Категория')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    img = models.ManyToManyField(Images)
    comment = models.TextField(null=True, blank=True)
    status_pin = models.ForeignKey('StatusPin', on_delete=models.PROTECT, blank=True)

    class Meta:
        verbose_name_plural = 'Нарушения'
        verbose_name = 'Нарушение'

    def __str__(self):
        return self.title


class StatusPin(models.Model):
    title = models.CharField(max_length=250, verbose_name='Статус нарушения')

    class Meta:
        verbose_name_plural = 'Cтатусы нарушений'
        verbose_name = 'Статус нарушения'

    def __str__(self):
        return self.title


class Crowdfunding(models.Model):
    title = models.CharField(max_length=240, verbose_name="Название")
    want = models.FloatField()
    have = models.FloatField()
