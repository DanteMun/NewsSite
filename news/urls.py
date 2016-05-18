from django.conf.urls import url


urlpatterns=[
    url(r'^$', 'news.views.index', name="index"),
    url(r'^(?P<pk>\d+)/$', 'news.views.post_detail', name="post_detail"),
    url(r'^new/$', 'news.views.post_new', name="post_new"),

    url(r'^(?P<post_pk>\d+)/comments/new/$', 'news.views.comment_new', name="comment_new")

]