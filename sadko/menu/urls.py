from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('category/<slug:category_slug>/', views.DishByCategoryView.as_view(),
         name='dish-cat-list')
]
