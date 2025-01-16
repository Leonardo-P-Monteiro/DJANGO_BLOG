from django.contrib import admin
from blog.models import Tag, Category
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {'slug': ('name',),}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {'slug': ('name',),}
