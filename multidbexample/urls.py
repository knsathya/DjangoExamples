from django.conf.urls import url, include
from django.contrib import admin
import multidbexample.views
urlpatterns = [
    url(r'^index.html$', multidbexample.views.IndexPageView.as_view(), name='index_page_view'),
    url(r'^add_publisher$', multidbexample.views.PublisherCreate.as_view(), name='add_publisher'),
    url(r'^edit_publisher/(?P<pk>\d+)$', multidbexample.views.PublisherUpdate.as_view(), name='edit_publisher'),
    url(r'^delete_publisher/(?P<pk>\d+)$', multidbexample.views.PublisherDelete.as_view(), name='delete_publisher'),
    url(r'^add_author$', multidbexample.views.AuthorCreate.as_view(), name='add_author'),
    url(r'^edit_author/(?P<pk>\d+)$', multidbexample.views.AuthorUpdate.as_view(), name='edit_author'),
    url(r'^delete_author/(?P<pk>\d+)$', multidbexample.views.AuthorDelete.as_view(), name='delete_author'),
	url(r'^(?P<page>.+\.html)$', multidbexample.views.load_page, name='load_page'),
    url(r'^$', multidbexample.views.hello),
]