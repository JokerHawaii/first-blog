from django.conf.urls import url
from django.contrib import admin

from .views import (
	profile_update
	)

urlpatterns = [
	# url(r'^$', post_list, name="list"),
	url(r'^update/$', profile_update, name="update"),
]