from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from . models import Post

class BlogHomeListView(ListView):
    template_name = 'MY_BLOG/index.html'
    queryset = Post.objects.all()

class PostDetailsView(DetailView):
    template_name = 'MY_BLOG/post.html'
