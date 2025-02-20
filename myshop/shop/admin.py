from django.contrib import admin

from shop.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','price',
                    'description', 'available', 'created',
                    'update']
    list_filter = ['available', 'created', 'update']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug':('name',)}