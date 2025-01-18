from django.db import models
from utils.rands import slugify_new
from utils.images import resize_image
from django.contrib.auth.models import User
from django_summernote.models import AbstractAttachment

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

        # This is the slug field config.
        if not self.slug:
            self.slug = slugify_new(self.title, k=4)

        # Here is the formatting of cover file.
        current_cover_name = str(self.cover.name)
        cover_changed = False

        super_save = super().save(*args, **kwargs) # Aqui estamos salvado o que 
        # foi passado de informação nova pelo forms desse nosso model.

        if self.cover:
            cover_changed = current_cover_name != self.cover.name
        
        if cover_changed:
            resize_image(self.cover, 900)

        return super_save

    def __str__(self) -> str:
        return self.title

class PostAttachment(AbstractAttachment):
    

    def save(self, *args, **kwargs):
        
        # This two lines below were brought across the copy of code excerpt of
        # the AbstractAttechment. We gone at the models Summernote to take this
        # excerpt. 
        if not self.name:
            self.name = self.file.name
        
        #This code snippet below was made by us.
        #Here is the formatting of file.
        current_file_name = str(self.file.name)
        file_changed = False

        super_save = super().save(*args, **kwargs) # Aqui estamos salvado o que 
        # foi passado de informação nova pelo forms desse nosso model.

        if self.file:
            file_changed = current_file_name != self.file.name
        
        if file_changed:
            resize_image(self.file, 900)

        return super_save
