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
    images = ImageSerializer(many=True)

    class Meta:
        model = Dish
        fields = ('title', 'description', 'price', 'images')
