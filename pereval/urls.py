from django.urls import path, include
from rest_framework import routers

from pereval.views import *

router = routers.SimpleRouter()
router.register(r'pereval', PerevalViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
