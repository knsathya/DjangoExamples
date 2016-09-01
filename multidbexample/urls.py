from django.conf.urls import url, include
from django.contrib import admin
import multidbexample.views
urlpatterns = [
    url(r'^index.html$', multidbexample.views.IndexPageView.as_view(), name='index_page_view'),
    url(r'^add_publisher$', multidbexample.views.PublisherCreate.as_view(), name='add_publisher'),
    url(r'^add_author$', multidbexample.views.AuthorCreate.as_view(), name='add_author'),
	url(r'^(?P<page>.+\.html)$', multidbexample.views.load_page, name='load_page'),
    url(r'^$', multidbexample.views.hello),
]