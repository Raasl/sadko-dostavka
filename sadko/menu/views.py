from django.shortcuts import render
from rest_framework import generics
from .models import Category, Dish
from .serializers import CategorySerializer, DishSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DishByCategoryView(generics.ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        return Dish.objects.filter(category__slug=category_slug)
