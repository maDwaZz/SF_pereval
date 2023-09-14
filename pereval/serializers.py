from rest_framework import serializers

from pereval.models import *


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'
