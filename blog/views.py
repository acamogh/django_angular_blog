from django.shortcuts import render
from rest_framework import generics,authentication,viewsets,permissions
from .models import Post,Comment
from .serializer import PostSerializer,CommentSerializer
import json

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