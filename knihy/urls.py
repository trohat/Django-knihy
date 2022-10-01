
from django.urls import path

from . import views

urlpatterns = [
    path("", views.NovaKniha2.as_view(), name="formular"),
    path("dekuji", views.dekuji, name="podekovani"),
    path("seznam", views.seznam, name="seznam_knih"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("form", views.my_form, name="my_form")
]


