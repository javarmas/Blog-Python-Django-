from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # The name of the template that is on urls file


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'  # The name of the template that is on urls file
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']  # We list the specific fields to be edited instead of using __all__ because we assume
    # that the author of the post will be the same, so we just want to edit the title and the body.


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')  # reverse_lazy won't execute the URL redirect until the view has finished
    # deleting the blog post
