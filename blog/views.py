from django.shortcuts import render,redirect
from rest_framework import generics,authentication,viewsets,permissions
import json

from .models import Post,Comment
from .serializer import PostSerializer,CommentSerializer
from .forms import PostForm

# Create your views here.
def home (request):
    return render(request, 'index.html', {})

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



def add_comments(request):
    if 'application/json' in request.META['CONTENT_TYPE']:
        print 'hi'
        data = json.loads(request.body)

        comment = data.get('comments', None)
        id = data.get('id', None)
        title = data.get('title', None)
        print comment,id,title
        #
        post = Post.objects.get(id = id)
        com = Comment()
        com. comments = comment
        com.title = post
        com.save()

    return render(request, 'index.html', {})

def add_post(request):
    forms = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        print form
        if form.is_valid():
            uncommit = form.save(commit=False)
            title= form.cleaned_data['title']
            description=form.cleaned_data['description']
            form.save()
            return redirect("home")
        else:
          print form.errors
    else:
        form = PostForm()
    return render(request, "add_post.html", {'forms': forms})