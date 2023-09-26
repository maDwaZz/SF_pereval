from rest_framework import serializers

from pereval.models import *


class PerevalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalUser
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ('level_winter', 'level_summer', 'level_autumn', 'level_spring')


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ('data',)


class PerevalAddedSerializer(serializers.ModelSerializer):
    user = PerevalUserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    image = PerevalImagesSerializer()

    class Meta:
        model = PerevalAdded
        fields = ('beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level',
                  'image')
