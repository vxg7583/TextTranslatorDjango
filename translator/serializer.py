from rest_framework import serializers
from .models import Translator

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
