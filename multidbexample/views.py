from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import RequestContext, TemplateDoesNotExist
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, FormView, View
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
import multidbexample.forms as multidbexampleforms
import multidbexample.models as multidbexamplemodels

# Create your views here.
def hello(request):
    return HttpResponse("Hi, Hello world")

def load_page(request, page):
    print page
    print "inside_load_page()"
    return render(request, page, {})
