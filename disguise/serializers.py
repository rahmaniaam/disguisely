from rest_framework import serializers

from .models import Disguise, Document

class DisguiseSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Disguise
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Document
        fields = '__all__'