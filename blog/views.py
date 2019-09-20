from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from blog.models import Tag, Post, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    # content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(
    #     category_id=category_id,
    #     tag_id=tag_id
    # )
    # return HttpResponse(content)

    # return render(request, 'blog/list.html', context={'name': 'post_list'})
    tag = None
    category = None

    # if tag_id:
    #     try:
    #         tag = Tag.objects.get(id=tag_id)
    #     except Tag.DoesNotExist:
    #         post_list = []
    #     else:
    #         post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    # else:
    #     post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
    #     if category_id:
    #         try:
    #             category = Category.objects.get(id=category_id)
    #         except Category.DoesNotExist:
    #             category = None
    #         else:
    #             post_list = post_list.filter(category_id=category_id)

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, tag = Post.get_bt_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    # return HttpResponse('detail')
    # return render(request, 'blog/detail.html', context={'name': 'post_detail'})

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        'sidebar': SideBar.get_all(),
    }
    context.update(Category.get_navs())

    return render(request, 'blog/detail.html', context=context)