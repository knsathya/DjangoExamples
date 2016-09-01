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

class PublisherCreate(CreateView):
    model = multidbexamplemodels.Publisher
    form_class = multidbexampleforms.PublisherForm
    success_url = reverse_lazy('index_page_view')

    def post(self, request, *args, **kwargs):
        print "Inside PublisherCreate post func()"
        print request.POST
        print self.success_url

        return super(PublisherCreate, self).post(request, *args, **kwargs)

class AuthorCreate(CreateView):
    model = multidbexamplemodels.Author
    form_class = multidbexampleforms.AuthorForm
    success_url = reverse_lazy('index_page_view')

    def post(self, request, *args, **kwargs):
        print "Inside AuthorCreate post func()"
        print request.POST
        print self.success_url

        return super(AuthorCreate, self).post(request, *args, **kwargs)

class IndexPageView(View):
    template_name ="index.html"
    context = {}
    def get(self, request, *args, **kwargs):
        print "index get func()1"
        self.context['publisher_list'] = multidbexamplemodels.Publisher.objects.all()
        self.context['author_list'] = multidbexamplemodels.Author.objects.all()

        return render(request, template_name=self.template_name, context=self.context)