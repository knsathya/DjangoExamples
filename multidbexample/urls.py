from django.conf.urls import url, include
from django.contrib import admin
import multidbexample.views
urlpatterns = [
	url(r'^(?P<page>.+\.html)$', multidbexample.views.load_page, name='load_page'),
    url(r'^$', multidbexample.views.hello),
]