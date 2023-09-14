from django.urls import path

from pereval.views import *

urlpatterns = [
    path('api/v1/pereval/submit-data', submitData),
]
