from rest_framework import serializers
from .models import Post

from App.serializers import UserCreateSerializer


class PostSerializer(serializers.ModelSerializer):
    created_by  = UserCreateSerializer(read_only=True)
    
    class Meta:        
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'image',
            'created_by',
            'created_at',
            'get_image',
        )
class PostRetrieveSerializer(serializers.ModelSerializer):
    created_by  = UserCreateSerializer(read_only=True)
    
    class Meta:        
        model = Post
      
        fields = (
            'id',
            'title',
            'content',
            'created_at',
            'created_by',
            'get_image',
            'image'
            
        )