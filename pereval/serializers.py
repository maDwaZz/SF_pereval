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
    data = serializers.URLField()

    class Meta:
        model = PerevalImages
        fields = ('data', 'title')


class PerevalAddedSerializer(drf_writable_nested.WritableNestedModelSerializer):
    user = PerevalUserSerializer()
    coords = CoordsSerializer()
    images = PerevalImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = ('id', 'beauty_title', 'title', 'other_titles', 'connect', 'user', 'coords', 'level_winter',
                  'level_summer', 'level_autumn', 'level_spring', 'images', 'status')

    def create(self, validated_data):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        images = validated_data.pop('images')

        pereval_user = PerevalUser.objects.filter(email=user['email'])
        if pereval_user.exists():
            user_serializer = PerevalUserSerializer(data=user)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()

        else:
            user = PerevalUser.objects.create(**user)
        coords = Coords.objects.create(**coords)
        pereval = PerevalAdded.objects.create(**validated_data, user=user, coords=coords)

        for image in images:
            data = image.pop('data')
            title = image.pop('title')
            print(title)
            PerevalImages.objects.create(data=data, pereval=pereval, title=title)

        return pereval



