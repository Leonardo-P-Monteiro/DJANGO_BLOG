from django.urls import path
from blog.views import PostListView, page, post, CreatedByList, \
    category, tag, search

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path(
        'created_by/<int:author_pk>/',
         CreatedByList.as_view(),
         name='created_by'
         ),
    path('category/<slug:slug>/', category, name='category'),
    path('tag/<slug:slug>/', tag, name='tag'),
    path('search/', search, name='search'),
]
