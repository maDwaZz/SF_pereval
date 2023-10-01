import drf_writable_nested
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from pereval.models import *


class PerevalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalUser
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ('data',)


class PerevalAddedSerializer(drf_writable_nested.WritableNestedModelSerializer):
    user = PerevalUserSerializer()
    coords = CoordsSerializer()
    # image = PerevalImagesSerializer()

    class Meta:
        model = PerevalAdded
        fields = ('beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level_winter',
                  'level_summer', 'level_autumn', 'level_spring')


    # def create(self, validated_data):
    #     images_data = validated_data.pop('image')
    #     pereval_added = PerevalAdded.objects.create(**validated_data)
    #
    #     for image_data in images_data:
    #         PerevalImages.objects.create(pereval=pereval_added, **images_data)
    #
    #     return pereval_added


    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     coords_data = validated_data.pop('coords')
    #     level_data = validated_data.pop('level')
    #     image_data = validated_data.pop('image')
    #     pereval_instance = PerevalAdded.objects.create(**validated_data, **level_data)
    #     PerevalUser.objects.create(**user_data)
    #     Coords.objects.create(**coords_data)
    #     PerevalImages.objects.create(**image_data)
    #     return pereval_instance


