from rest_framework import serializers
from .models import *

#Serializer class for the user data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'date_joined']


#Serializer class to retrieve,post and update the Notes data
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NOTE
        fields = '__all__'