from rest_framework import serializers
from .models import Webpage, Session, Viewer
from django.contrib.auth.models import User

class WebpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webpage
        fields = ['id', 'title', 'url']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'host', 'code', 'current_webpage', 'created_at']

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = ['id', 'session', 'identifier', 'joined_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
