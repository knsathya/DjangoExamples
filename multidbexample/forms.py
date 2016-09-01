from django.forms import ModelForm
from django import forms
from django.http.request import QueryDict
import multidbexample.models as multidbexample


class PublisherForm(ModelForm):
    class Meta:
        model = multidbexample.Publisher
        fields = '__all__'

class AuthorForm(ModelForm):
    class Meta:
        model = multidbexample.Author
        fields = '__all__'