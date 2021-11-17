from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
        class Meta:
            model = BlogPost
            fields = ['title', 'link', 'date', 'artist_name', 'location']

