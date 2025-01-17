from django.db import models
from utils.rands import slugify_new
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True, default=None, 
                            max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, k=4)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique= True, default=None, null=True, blank=True,
                            max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, k=4)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    title = models.CharField(max_length=200,)
    slug = models.SlugField(max_length=255, unique=True, default="", null=False,
                            blank=True,)
    is_published = models.BooleanField(default=False, help_text="This field \
                                       need to be marked for the page will be \
                                       shown." )
    content = models.TextField(default=None, null=True,)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, k=4)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    title = models.CharField(max_length=65,)
    slug = models.SlugField(max_length=255, unique=True, default='', null=True,
                            blank=True)
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False, help_text='This field need \
                                     to be marked for the page will be shown')
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='',)
    cover_in_post_content = models.BooleanField(default=True, help_text='If \
                                                this field will marked, \
                                                it will show the cover into the \
                                                post.',)
    created_at = models.DateTimeField(auto_now_add=True,)
    created_by = models.ForeignKey(User, blank=True, null=True, 
                                 on_delete=models.SET_NULL, 
                                 related_name='post_created_by',)
    updated_at = models.DateTimeField(auto_now=True,)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='post_updated_by')
    category = models.ForeignKey(Category, models.SET_NULL, null=True,
                                 blank=True, default=None,)
    tags = models.ManyToManyField(Tag, blank=True, default='',)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify_new(self.title, k=4)

        return super().save(*args, *kwargs)
    
    def __str__(self) -> str:
        return self.title