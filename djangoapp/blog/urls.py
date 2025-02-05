from django.urls import path
from blog.views import PostListView, PageDatailView, post, CreatedByList, \
    CategroyListView, TagListView, SearchListView

app_name = 'blog'

urlpatterns = [
    path(
        '',
         PostListView.as_view(),
         name='index'
         ),
    path(
        'post/<slug:slug>/',
         post,
         name='post'
         ),
    path(
        'page/<slug:slug>/',
         PageDatailView.as_view(),
         name='page'
         ),
    path(
        'created_by/<int:author_pk>/',
         CreatedByList.as_view(),
         name='created_by'
         ),
    path(
        'category/<slug:slug>/',
         CategroyListView.as_view(),
          name='category'
         ),
    path(
        'tag/<slug:slug>/',
         TagListView.as_view(),
         name='tag'
         ),
    path(
        'search/',
        SearchListView.as_view(),
        name='search'
         ),
]
