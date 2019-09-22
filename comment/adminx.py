import xadmin
from django.contrib import admin

# Register your models here.
from comment.models import Comment
from typeidea.custom_site import custom_site


@xadmin.sites.register(Comment)
class CommentAdmin:
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')