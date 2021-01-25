from rest_framework import serializers
from .models import Event

class Eventserializer(serializers.EventSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post
