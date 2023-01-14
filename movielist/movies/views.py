from django.shortcuts import render
from django.views.generic import TemplateView


class MovieView(TemplateView):
    template_name = 'index.html'




# fra; https://www.bugbytes.io/posts/django-unicorn-an-introduction/