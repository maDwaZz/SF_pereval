from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from pereval.models import *
from pereval.serializers import *


# class PerevalAPIView(APIView):
#     def get(self, request):
#         p = PerevalAdded.objects.all()
#         return Response({'pereval_items': PerevalSerializer(p, many=True).data})
#
#     def post(self, request):
#         pereval_serializer = PerevalSerializer(data=request.data)
#         # coords_serializer = CoordsSerializer(data=request.data)
#         # pereval_images_serializer = PerevalImagesSerializer(data=request.data)
#         # total_serializer = pereval_serializer + coords_serializer + pereval_images_serializer
#         # total_serializer.is_valid(raise_exception=True)
#         # total_serializer.save()
#         pereval_serializer.is_valid(raise_exception=True)
#         pereval_serializer.save()
#
#         return Response({'pereval_item': pereval_serializer.data})


@api_view(['POST'])
def submitData(request):
    serializer = PerevalAddedSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'pereval_item': serializer.data})
