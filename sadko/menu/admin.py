from django import forms
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.utils.html import format_html

from .models import Category, Dish, DishImage


@admin.action(description='Отобразить на сайте')
def make_published(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Убрать отображение на сайте')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_active=False)


class DishImageInline(SortableTabularInline):
    model = DishImage
    extra = 1
    readonly_fields = ('get_image',)
    fields = ('image', 'get_image', 'is_active')

    @admin.display(description='Просмотр')
    def get_image(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100">')
        return '---'


class DishInline(SortableTabularInline):
    model = Dish
    show_change_link = True
    extra = 0


class MyDishAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Dish
        fields = '__all__'


@admin.register(Dish)
class DishAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ('title', 'slug', 'category', 'show_price',
                    'show_weight', 'is_active', 'position')
    list_display_links = ('title', 'slug')
    list_editable = ('is_active',)
    list_filter = ('category', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category__title')
    sortable_by = ()
    inlines = (DishImageInline,)
    form = MyDishAdminForm
    actions = (make_published, make_unpublished)

    @admin.display(description='Цена')
    def show_price(self, obj):
        return str(obj.price) + ' ₽'
    
    @admin.display(description='Вес')
    def show_weight(self, obj):
        return str(obj.weight) + ' г.'


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'show_amount_dishes',
                    'is_active', 'position')
    list_display_links = ('title', 'slug')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}
    sortable_by = ()
    inlines = (DishInline,)

    @admin.display(description='Кол-во в категории / на сайте')
    def show_amount_dishes(self, obj):
        in_cat = obj.dishes.all().count()
        published = obj.dishes.filter(is_active='True').count()
        return f"{in_cat} / {published}"
