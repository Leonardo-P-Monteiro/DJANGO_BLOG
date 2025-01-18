from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from blog.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin

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

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = 'content',
    list_display = 'title', 'slug',
    list_display_links = 'title',
    search_fields = 'title', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'content',
    list_display = 'id', 'title', 'is_published', 'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'slug', 'content',
    list_per_page = 50
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by',
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = 'tags', 'category',

    # Here we are 
    def save_model(self, request: HttpRequest, obj: Post, form: ModelForm,
                   change: bool) -> None:
        
        if change:
            obj.updated_by = request.user #type: ignore
        else:
            obj.created_by = request.user #type: ignore

        return super().save_model(request, obj, form, change)