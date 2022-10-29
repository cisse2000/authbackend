from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from App_document.models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'name',
            'file'
            
        )