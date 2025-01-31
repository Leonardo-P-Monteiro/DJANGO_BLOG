from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post, Page
from django.db.models import Q
from django.http import HttpRequest, Http404
from django.contrib.auth.models import User


PER_PAGE = 9

def index(request):
    posts = Post.objects2.get_published() 
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Home - ',
        }
    )

def created_by(request, author_pk):
    posts = (Post.objects2.get_published()
             .filter(created_by__pk = author_pk))
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    user = User.objects.filter(pk=author_pk).first()

    if user == None:
        raise Http404()
    
    user_full_name = user.username

    if user.first_name:
        user_full_name = f'Posts de {user.first_name} {user.last_name} - ' 

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': user_full_name,
        }
    )

def category(request, slug):
    posts = (Post.objects2.get_published()
             .filter(category__slug=slug)
             )
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title= f'{page_obj[0].category.name} - Category - ' 

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )

def tag(request, slug):
    posts = (Post.objects2.get_published()
             .filter(tags__slug=slug)
             )
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404() 

    page_title= f'{page_obj[0].tags.first().name} - Tags - ' 

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
        }
    )

def page(request, slug):
    
    page = (
        Page.objects.filter(slug=slug).first()
             )

    if page is None:
        raise Http404()

    page_title = f'{page.title} - '

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page,
            'page_title': page_title,
        }
    )

def post(request, slug):

    post = (
        Post.objects2.get_published()
        .filter(slug=slug)
        .first()
             )
    
    if post is None:
        raise Http404()
    
    page_title = f'{post.title} - '

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
            'page_title': page_title,
        }
    )

def search(request: HttpRequest):
    search_value = request.GET.get('search', '').strip()
    posts = (Post.objects2.get_published()
             .filter(
                Q(title__icontains= search_value) |
                Q(excerpt__icontains= search_value) |
                Q(content__icontains= search_value)
                )
             )
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page_title = f'{search_value[:20]} - '

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'search_value': search_value,
            'page_title': page_title,
        }
    )