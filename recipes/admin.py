from django.contrib import admin
from .models import Category, Recipe

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
