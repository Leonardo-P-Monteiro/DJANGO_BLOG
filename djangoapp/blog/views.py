from typing import Any
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from blog.models import Post, Page
from django.db.models import Q
from django.http import HttpRequest, Http404, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


PER_PAGE = 9

class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts' # Essa variável é que vai conter no context
    # a lista de objetos retornada pelo queryset.
    ordering = '-pk' # Este atributo é herança de mixin. Na documentação você o
    #verá em Mixins e não na explicação da ListView.
    paginate_by = PER_PAGE
    queryset = Post.objects2.get_published() # Aqui estamos definindo a queryset
    # de busca dos dados que queremos. Mas também podemos fazer da forma que 
    # deixei a baixo.

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_published = True) # Aqui nós estamos apenas
    #     # adicionando um filtro na queryset original. Mas essa forma aqui é melhor
    #     # para as situações em que é necessário fazer buscas dinâmicas, cujos 
    #     # parâmetros variem. Usa aquela propriedade "queryset" e fornece uma
    #     # queryset.
    #     return queryset

    def get_context_data(self, **kwargs): # Aqui 
        context = super().get_context_data(**kwargs)
        context['page_tititle'] = 'Home - '

        return context

#EXEMPLO DO MESMO PROCESSO DA PostListView.
# def index(request):
#     posts = Post.objects2.get_published() 
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         'blog/pages/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title': 'Home - ',
#         }
#     )

class CreatedByList(PostListView):
    
    def get(self, request, *args, **kwargs):
        
        author_pk = self.kwargs.get('author_pk', '')
        user = User.objects.filter(pk=author_pk).first() # Colocamos o "first" 
        # para recebermos apenas um item, e não uma lista.

        if user is None:
            return Http404()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(pk=self.kwargs.get('author_pk', '')).first()
        user_full_name = user.username #type: ignore     
        
        if user.first_name: #type: ignore     
            user_full_name = f'Post de {user.first_name} {user.last_name} - ' #type:ignore     
        
        context.update({'page_title':user_full_name})

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(created_by=self.kwargs.get('author_pk', ''))

        return queryset

# def created_by(request, author_pk):
#     posts = (Post.objects2.get_published()
#              .filter(created_by__pk = author_pk))
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     user = User.objects.filter(pk=author_pk).first()

#     if user == None:
#         raise Http404()
    
#     user_full_name = user.username

#     if user.first_name:
#         user_full_name = f'Posts de {user.first_name} {user.last_name} - ' 

#     return render(
#         request,
#         'blog/pages/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title': user_full_name,
#         }
#     )


class CategroyListView(PostListView):

    def get_queryset(self):
        return super().get_queryset().filter(
            category__slug=self.kwargs.get('slug', '')
            )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        page_title = (f'{self.object_list[0].category.name}' #type: ignore
                       ' - Categoria - ') 
        context.update({
            'page_title':page_title
        })

        return context

# def category(request, slug):
#     posts = (Post.objects2.get_published()
#              .filter(category__slug=slug)
#              )
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     if len(page_obj) == 0:
#         raise Http404()

#     page_title= f'{page_obj[0].category.name} - Category - ' 

#     return render(
#         request,
#         'blog/pages/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title': page_title,
#         }
#     )



class TagListView(PostListView):

    def get_queryset(self):
        return super().get_queryset().filter(
            category__slug=self.kwargs.get('slug', '')
            )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        page_title = (f'{self.object_list[0].tags.name}' #type: ignore
                       ' - Tag - ') 
        context.update({
            'page_title':page_title
        })

        return context


# def tag(request, slug):
#     posts = (Post.objects2.get_published()
#              .filter(tags__slug=slug)
#              )
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     if len(page_obj) == 0:
#         raise Http404() 

#     page_title= f'{page_obj[0].tags.first().name} - Tags - ' 

#     return render(
#         request,
#         'blog/pages/index.html',
#         {
#             'page_obj': page_obj,
#             'page_title': page_title,
#         }
#     )

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/pages/page.html'
    slug_field = 'slug'
    context_object_name = 'page'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.get_object()
        page_title = f'{page.title} - ' #type:ignore
        context.update({
            'page_title': page_title
        })
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)

# def page(request, slug):
    
#     page = (
#         Page.objects.filter(slug=slug).first()
#              )

#     if page is None:
#         raise Http404()

#     page_title = f'{page.title} - '

#     return render(
#         request,
#         'blog/pages/page.html',
#         {
#             'page': page,
#             'page_title': page_title,
#         }
#     )

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/pages/post.html'
    # slug_field = 'slug' Por padrão esse atributo já é preechido exatamente como está em nosso script. 
    # por isso é bom já construir o model com o campo slug literalmente chamando ele de slug.
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        page_title = f'{post.title} - ' #type:ignore
        context.update({
            'page_title': page_title
        })
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)

# def post(request, slug):

#     post = (
#         Post.objects2.get_published()
#         .filter(slug=slug)
#         .first()
#              )
    
#     if post is None:
#         raise Http404()
    
#     page_title = f'{post.title} - '

#     return render(
#         request,
#         'blog/pages/post.html',
#         {
#             'post': post,
#             'page_title': page_title,
#         }
#     )


class SearchListView(PostListView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_value = ''

    def setup(self, request, *args, **kwargs):
        self.search_value = request.GET.get('search', '').strip()
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
                Q(title__icontains= self.search_value) | #type: ignore
                Q(excerpt__icontains= self.search_value) | #type: ignore
                Q(content__icontains= self.search_value) #type: ignore
                )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.search_value
        return context
    
    
    def get(self, request, *args, **kwargs):
        if self.search_value == '':
            return redirect('blog:index')

        return super().get(request, *args, **kwargs)

# def search(request: HttpRequest):
#     search_value = request.GET.get('search', '').strip()
#     posts = (Post.objects2.get_published()
#              .filter(
#                 Q(title__icontains= search_value) |
#                 Q(excerpt__icontains= search_value) |
#                 Q(content__icontains= search_value)
#                 )
#              )
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     page_title = f'{search_value[:20]} - '

#     return render(
#         request,
#         'blog/pages/index.html',
#         {
#             'page_obj': page_obj,
#             'search_value': search_value,
#             'page_title': page_title,
#         }
#     )