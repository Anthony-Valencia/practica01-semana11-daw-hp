# catalogo/urls.py
from django.urls import path
from . import views

app_name = "catalogo"  # Namespace para usar {% url 'catalogo:lista' %}

urlpatterns = [
    path("", views.ProductoListView.as_view(), name="lista"),
]
