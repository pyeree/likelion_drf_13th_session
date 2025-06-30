from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    comments = serializers.SerializerMethodField(read_only=True)
    tags = serializers.SerializerMethodField()


    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments, many=True)
        return serializer.data

    def get_tags(self,instance):
        tag = instance.tags.all()
        return [t.name for t in tag]
    class Meta:
        model = Movie
        #fields = ['id', 'name', 'content', 'created_at', 'updated_at', 'comments', 'tags'] # tags 추가!
        fields = '__all__'
        # fields = ('id', 'name', 'content', 'created_at', 'updated_at')
    
    image = serializers.ImageField(use_url=True,required=False)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['movie']