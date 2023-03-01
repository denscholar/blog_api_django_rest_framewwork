from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # To add validations
    title = serializers.CharField(max_length=30)
    
    class Meta:
      model =  Post
      fields = '__all__'