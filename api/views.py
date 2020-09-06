from rest_framework import generics
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from Pin.models import Pin, Category, StatusPin, Images, Crowdfunding
from .serializers import PinSerializer, CategorySerializer, UserSerializer, \
    CategoryCountSerializer, StatusSerializers, CrowdfundingSerializer, ImagesSerializers


# Create your views here.
class PinList(generics.ListCreateAPIView):
    """Список нарушений"""
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    """Нарушение по идентификатору"""
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class UserList(generics.ListCreateAPIView):
    """Список зарегестрированных пользователей"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Пользователь по идентификатору"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CategoryList(generics.ListCreateAPIView):
    """Список категорий нарушений"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """Категория по идентификатору"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StatusList(generics.ListCreateAPIView):
    """Статусы нарушений"""
    queryset = StatusPin.objects.all()
    serializer_class = StatusSerializers


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """Статус нарушения"""
    queryset = StatusPin.objects.all()
    serializer_class = StatusSerializers


class CategoryCount(generics.ListAPIView):
    """Количество категорий нарушений"""
    queryset = str(len(Category.objects.all()))
    serializer_class = CategoryCountSerializer


class ImagesList(generics.ListCreateAPIView):
    """Список картинок"""
    queryset = Images.objects.all()
    serializer_class = ImagesSerializers


class ImagesDetail(generics.RetrieveUpdateDestroyAPIView):
    """Картинка по идентификатору"""
    queryset = Images.objects.all()
    serializer_class = ImagesSerializers


class CrowdfundingList(generics.ListCreateAPIView):
    """"""
    queryset = Crowdfunding.objects.all()
    serializer_class = CrowdfundingSerializer


class CrowdfundingDetail(generics.RetrieveUpdateDestroyAPIView):
    """"""
    queryset = Crowdfunding.objects.all()
    serializer_class = CrowdfundingSerializer
