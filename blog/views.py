from django.shortcuts import render, get_object_or_404
from datetime import date
from django.http import Http404
from .models import Post, Author, Tag



def starting_page(request):
    return render(request, "blog/index.html", {"posts": Post.objects.order_by("-date")[:3]})

def posts(request):
    return render(request, "blog/posts.html", {"posts" : Post.objects.order_by("-date")})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
        
def authors(request):
    return render(request, "blog/authors.html", {"authors" : Author.objects.all()})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, "blog/author_detail.html", {"author": author})

def tags(request):
    return render(request, "blog/tags.html", {"tags" : Tag.objects.all()})

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    return render(request, "blog/tag_detail.html", {"tag" : tag})