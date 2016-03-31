from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	post_archive,
	post_about,
	post_share,
	)

urlpatterns = [
	url(r'^$', post_list, name="list"),
	url(r'^archives/$', post_archive, name="archive"),
	url(r'^about/$', post_about),
	url(r'^create/$', post_create),
	url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),
	url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
	url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
	url(r'^(?P<slug>[\w-]+)/share/$', post_share, name='share'),
	url(r'^tag/(?P<tag_slug>[\w-]+)/$', post_list, name='post_list_by_tag'),
]