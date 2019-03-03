from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView



class IndexTemplateView(TemplateView):
    template_name = 'MY_BLOG/index.html'
