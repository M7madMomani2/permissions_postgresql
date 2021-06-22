from django.db import models
from rest_framework import serializers
from .models import Posts 

class Postserializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title', 'body' , 'create_at','updated_at')
        model = Posts