from rest_framework import serializers

from pereval.models import *


class PerevalSerializer(serializers.Serializer):
    beauty_title = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField()
    add_time = serializers.DateTimeField()
    email = serializers.EmailField(source=user.email)
    fam = serializers.CharField(source=user.last_name)
    name = serializers.CharField(source=user.first_name)
    latitude = serializers.FloatField()
    longtitude = serializers.FloatField()
    height = serializers.IntegerField()
    level_winter = serializers.CharField()
    level_summer = serializers.CharField()
    level_autumn = serializers.CharField()
    level_spring = serializers.CharField()

