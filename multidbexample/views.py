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
        print self.template_name
        print self.template_name_suffix

        return super(PublisherCreate, self).post(request, *args, **kwargs)

class PublisherUpdate(UpdateView):
    model = multidbexamplemodels.Publisher
    template_name ="add_entry.html"
    form_class = multidbexampleforms.PublisherForm
    success_url = reverse_lazy('index_page_view')

    def get_object(self):
        print "Inside publisher update get object"

        if 'pk' not in self.kwargs.keys():
            return None

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return obj

class PublisherDelete(DeleteView):
    model = multidbexamplemodels.Publisher
    template_name ="delete_entry.html"
    form_class = multidbexampleforms.PublisherForm
    context = []
    success_url = reverse_lazy('index_page_view')

    def get_object(self):
        print "Inside publisher delete get object"

        if 'pk' not in self.kwargs.keys():
            return None

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return obj

    def get_context_data(self, **kwargs):
        self.context = super(PublisherDelete, self).get_context_data(**kwargs)
        self.context['class_name'] = "Publisher"
        self.context['obj_name'] = self.get_object()

        return self.context

class AuthorCreate(CreateView):
    model = multidbexamplemodels.Author
    form_class = multidbexampleforms.AuthorForm
    success_url = reverse_lazy('index_page_view')

    def post(self, request, *args, **kwargs):
        print "Inside AuthorCreate post func()"
        print request.POST
        print self.success_url

        return super(AuthorCreate, self).post(request, *args, **kwargs)

class AuthorUpdate(UpdateView):
    model = multidbexamplemodels.Author
    template_name ="add_entry.html"
    form_class = multidbexampleforms.AuthorForm
    success_url = reverse_lazy('index_page_view')

    def get_object(self):
        print "Inside author update get object"

        if 'pk' not in self.kwargs.keys():
            return None

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return obj

class AuthorDelete(DeleteView):
    model = multidbexamplemodels.Author
    template_name ="delete_entry.html"
    form_class = multidbexampleforms.AuthorForm
    context = []
    success_url = reverse_lazy('index_page_view')

    def get_object(self):
        print "Inside author delete get object"

        if 'pk' not in self.kwargs.keys():
            return None

        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])

        return obj

    def get_context_data(self, **kwargs):
        self.context = super(AuthorDelete, self).get_context_data(**kwargs)
        self.context['class_name'] = "Author"
        self.context['obj_name'] = self.get_object()

        return self.context

class IndexPageView(View):
    template_name ="index.html"
    context = {}
    def get(self, request, *args, **kwargs):
        print "index get func()1"
        self.context['publisher_list'] = multidbexamplemodels.Publisher.objects.all()
        self.context['author_list'] = multidbexamplemodels.Author.objects.all()

        return render(request, template_name=self.template_name, context=self.context)