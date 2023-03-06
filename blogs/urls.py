from django.urls import path
from .views import PostListView, PostDetailView

app_name = "blogs"

urlpatterns = [
    path("blogs/", PostListView.as_view(), name="post_list"),
    path("blog/<slug>/", PostDetailView.as_view(), name="post_detail"),
]
