from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed

from blog.models import Post


class ExtendedRssFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRssFeed, self).add_item_elements(handler, item)
        handler.addQuickElement('content:html', item['content_html'])


class LatestPostFeed(Feed):
    feed_type = ExtendedRssFeed
    title = 'Typeidea Blog System'
    link = '/rss/'
    description = 'typeidea is a blog system power by ohana'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    def item_link(self, item):
        return reverse('post-detail', args=[item.pk])

    def item_extra_kwargs(self, item):
        return {'content_html': self.item_content_html(item)}

    def item_content_html(self, item):
        return item.content_html
