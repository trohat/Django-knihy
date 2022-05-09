
from django.urls import path

from . import views

urlpatterns = [
    path("", views.nova_kniha, name="formular"),
    path("dekuji", views.dekuji, name="podekovani")
]


