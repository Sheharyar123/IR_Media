from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blogs/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return Post.objects.filter(is_active=True)
