# catalogo/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


# ---------- FBV: Vista basada en función ----------
def home(request):
    """Página de inicio: muestra un mensaje y los 3 productos más recientes."""
    ultimos_productos = Producto.objects.all()[:3]
    contexto = {
        "titulo": "Bienvenido a Café Aurora",
        "ultimos_productos": ultimos_productos,
    }
    return render(request, "home.html", contexto)


# ---------- CBV: Vista basada en clase ----------
class ProductoListView(ListView):
    """Listado completo de productos disponibles."""

    model = Producto
    template_name = "catalogo/lista.html"
    context_object_name = "productos"  # Nombre en la plantilla
    queryset = Producto.objects.filter(disponible=True)  # Solo disponibles
