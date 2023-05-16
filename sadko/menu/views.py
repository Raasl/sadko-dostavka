from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from .models import Category, Dish
from .serializers import CategorySerializer, DishSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class DishByCategoryView(views.APIView):
    def get(self, request, category_slug):
        try:
            category = Category.objects.get(slug=category_slug,
                                            is_active=True)
        except Category.DoesNotExist:
            return Response({'error': 'Category is not found'},
                            status=status.HTTP_404_NOT_FOUND)
        qs = Dish.objects.filter(category=category, is_active=True)
        serializer = DishSerializer(qs, many=True)
        return Response(serializer.data)
