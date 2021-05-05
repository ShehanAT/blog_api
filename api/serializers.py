from rest_framework import serializers 
from .models import Post 

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post 
        fields = ('author', 'author_id', 'likes', 'popularity', 'reads', 'tags')