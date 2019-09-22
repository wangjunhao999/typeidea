"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path, re_path

from blog.rss import LatestPostFeed
from blog.sidemap import PostSitemap
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView, LinkListView
from comment.views import CommentView
from typeidea.autocomplete import CategoryAutocomplete, TagAutocomplete
from typeidea.custom_site import custom_site
from config.views import links
from django.contrib.sitemaps import views as sitemap_views


urlpatterns = [
    path('admin/', xadmin.site.urls, name='xadmin'),

    path('category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path('tag-autocomplete/', TagAutocomplete.as_view(), name='tag-autocomplete'),

    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),

    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path('links/', LinkListView.as_view(), name='links'),
    path('comment/', CommentView.as_view(), name='comment'),

    path('rss/', LatestPostFeed(), name='rss'),
    re_path(r'^sitemap\.xml', sitemap_views.sitemap, {'sitemaps': {
        'posts': PostSitemap,
    }}),

]
