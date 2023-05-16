from typing import Iterable, Optional
from django.db import models
from django.core.validators import MaxValueValidator
from . import utils


class Category(models.Model):
    """Категории в меню"""

    title = models.CharField(
        verbose_name='Название категории',
        max_length=50,
        unique=True
    )

    slug = models.SlugField(
        max_length=50,
        verbose_name='URL',
        unique=True
    )

    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция',
        default=0
    )

    is_active = models.BooleanField(
        verbose_name='Отображать',
        default=False
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['position']
        indexes = [
            models.Index(fields=['position'])
        ]

    def __str__(self) -> str:
        return self.title

    @staticmethod
    def get_or_create_default_category():
        """Получить или создать категорию 'Все блюда'"""
        default_category, is_created = Category.objects.get_or_create(
            title='Все блюда',
            defaults={
                'position': 0,
                'is_active': False
            }
        )
        return default_category


class Dish(models.Model):
    """Позиции блюд в меню"""

    title = models.CharField(
        verbose_name='Наименование',
        max_length=100
    )

    slug = models.SlugField(
        max_length=100,
        verbose_name='URL',
        unique=True
    )

    description = models.CharField(
        max_length=255,
        verbose_name='Описание блюда',
        blank=True
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена',
        validators=[MaxValueValidator(
            limit_value=9999,
            message=f'Максимальная цена 9999р.'
        )]
    )

    weight = models.PositiveIntegerField(
        verbose_name='Вес',
        validators=[MaxValueValidator(
            limit_value=9999,
            message=f'Максимальный вес 9999г.'
        )]
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=Category.get_or_create_default_category,
        verbose_name='Категория',
        related_name='dishes'
    )

    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция',
        default=0
    )

    is_active = models.BooleanField(
        verbose_name='Отображать',
        default=False
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['position']
        indexes = [
            models.Index(fields=['position', 'title'])
        ]

    def __str__(self) -> str:
        return self.title


class DishImage(models.Model):
    """Картинки для позиций меню"""

    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Блюдо'
    )

    image = models.ImageField(
        upload_to=utils.get_image_path_name,
        verbose_name='Фото блюда',
        blank=True
    )

    position = models.PositiveSmallIntegerField(
        verbose_name='Позиция',
        default=0
    )

    is_active = models.BooleanField(
        verbose_name='Отображать',
        default=False
    )

    class Meta:
        verbose_name = 'Фотографии блюда'
        verbose_name_plural = 'Фотографии блюд'
        ordering = ['position']
        indexes = [
            models.Index(fields=['position'])
        ]

    def __str__(self) -> str:
        return self.image.url.split('/')[-1]
