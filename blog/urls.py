from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    BlogCreateView,
    BlogListView,
    BlogUpdateView,
    BlogDeleteView,
    BlogDetailView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/detail/", BlogDetailView.as_view(), name="blog_detail"),
    path("<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
