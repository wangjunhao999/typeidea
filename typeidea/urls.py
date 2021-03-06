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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from blog.apis import PostViewSet, CategoryViewSet
from blog.rss import LatestPostFeed
from blog.sidemap import PostSitemap
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView, LinkListView
from comment.views import CommentView
from typeidea.autocomplete import CategoryAutocomplete, TagAutocomplete
from typeidea.custom_site import custom_site
from config.views import links
from django.contrib.sitemaps import views as sitemap_views

router = DefaultRouter()
router.register('post', PostViewSet, base_name='api-post')
router.register('category', CategoryViewSet, base_name='api-category')

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
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('api/post/', PostList.as_view(), name='post-list'),
    path('api/', include(router.urls)),
    path('api/docs/', include_docs_urls(title='typeidea apis')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns