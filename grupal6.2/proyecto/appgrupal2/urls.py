
from django.urls import path

from .views import *

app_name = "appgrupal2"

urlpatterns = [
    path("", index_appgrupal2),
]
