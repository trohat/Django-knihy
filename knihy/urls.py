
from django.urls import path

from . import views

urlpatterns = [
    path("", views.NovaKniha2.as_view(), name="formular"),
    path("dekuji", views.Dekuji.as_view(), name="podekovani"),
    path("seznam", views.Seznam2.as_view(), name="seznam_knih"),
    path("detail/<int:pk>", views.Detail.as_view(), name="detail")
]


