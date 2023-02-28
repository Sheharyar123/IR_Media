from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blogs/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return Post.objects.filter(is_active=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "blogs/post_detail.html"
    context_object_name = "post"

    def get_object(self):
        queryset = get_object_or_404(Post, id=self.kwargs.get("pk"), is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["recent_posts"] = Post.objects.filter(is_active=True).exclude(
            id=post.id
        )[:3]
        context["post_tags"] = post.tags.all()
        return context
