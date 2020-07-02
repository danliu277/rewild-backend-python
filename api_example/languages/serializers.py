from rest_framework import serializers
from .model import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        paradigm = ('id', 'name', 'paradigm')