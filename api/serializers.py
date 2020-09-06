from django.contrib.auth import get_user_model
from rest_framework import serializers

from Pin.models import Pin, Category, StatusPin, Images, Crowdfunding
from decimal import Decimal


class LocationField(serializers.Serializer):
    lat_loc = serializers.DecimalField(source='lat', max_digits=14, decimal_places=12, )
    lng_loc = serializers.DecimalField(source='lng', max_digits=14, decimal_places=12, )


class PinSerializer(serializers.ModelSerializer):
    location = LocationField(source='*')

    class Meta:
        model = Pin
        fields = ('id', 'title', 'location', 'category', 'user', 'img', 'comment', 'status_pin')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'danger', 'image',)


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatusPin
        fields = ('id', 'title',)


class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'title', 'img',)


class CategoryCountSerializer(serializers.ModelSerializer):
    category_count = serializers.SerializerMethodField('get_category_count')

    class Meta:
        model = Category
        fields = ('category_count',)

    def get_category_count(self, obj):
        return Category.objects.all().count()


class CrowdfundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crowdfunding
        fields = ('id', 'title', 'want', 'have',)
