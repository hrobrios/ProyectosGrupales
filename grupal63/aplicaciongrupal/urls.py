
from django.urls import path
from .views import *

app_name="aplicaciongrupal"

urlpatterns = [
    path("", index_aplicaciongrupal)
]
