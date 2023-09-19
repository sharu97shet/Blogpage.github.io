from rest_framework import serializers
from Blog.models import *
from rest_framework.response import Response
import re
from django.db import models


class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloguser
        fields ='__all__'
        # fields = ('Name',
        #           'Email')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields ='__all__'
        # fields = ('BlogName',
        #           'city')

class BlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogdetails
        fields ='__all__'      

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields ='__all__'

        
class cityserializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields ='__all__'            

# class Newblogserializer(serializers.Serializer):
#     #id=models.CharField(max_length=200)

#     BlogName = serializers.CharField(label="enter blogname")

#     Image= serializers.ImageField(label="select  blog image")

#     Description=serializers.CharField(label="enter description")

#     user=serializers.CharField(label="enter bloguserid")

#     def __str__(self):
#         return self.BlogName          
        
   