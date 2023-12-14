from .models import *
from rest_framework import serializers



class newserializer(serializers.ModelSerializer):
    class Meta:
        model=news
        fields='__all__'


class hotelserializer(serializers.ModelSerializer):
    class Meta:
        model=hotels
        fields='__all__'


class productform(serializers.ModelSerializer):
    class Meta:
        model=productmodel
        fields='__all__'





class viewserial(serializers.ModelSerializer):
    class Meta:
        model=viewmodel
        fields='__all__'





class newyserial(serializers.ModelSerializer):
    class Meta:
        model=newywmodel
        fields='__all__'



class personserial(serializers.ModelSerializer):
    class Meta:
        model=personmodel
        fields='__all__'



class todoserializer(serializers.ModelSerializer):
    class Meta:
        model=todosmodel
        fields='__all__'
