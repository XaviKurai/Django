from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("authors", views.authors, name="authors-page"),
    path("authors/<int:authorid>", views.author_detail, name="author_detail"),
    path("tags", views.tags, name="tags-page"),
    path("tags/<int:tag_id>", views.tag_detail, name="tag_detail"),
]