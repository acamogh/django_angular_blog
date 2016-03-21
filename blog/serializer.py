from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="title.id", read_only=True)
    title = serializers.CharField(source="title.title", read_only=True)

    class Meta:
        model = Comment
        fields = ('id','title','comments')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','title','description','pub_date')
