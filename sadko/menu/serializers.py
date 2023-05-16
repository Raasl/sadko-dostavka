from .models import Category, Dish, DishImage
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = DishImage
        fields = ('image_url',)

    def get_image_url(self, obj):
        return obj.image.url


class DishSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Dish
        fields = ('id', 'title', 'description', 'price', 'weight', 'images')

    def get_images(self, obj):
        images = obj.images.filter(is_active=True)
        return ImageSerializer(images, many=True).data
