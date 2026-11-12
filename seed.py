# seed.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafe_aurora.settings")
django.setup()

from catalogo.models import Producto

productos = [
    {
        "nombre": "café americano",
        "descripcion": "Café negro de grano tostado medio.",
        "precio": 5.50,
        "stock": 20,
        "disponible": True,
    },
    {
        "nombre": "capuchino",
        "descripcion": "Espresso con leche vaporizada y espuma.",
        "precio": 7.90,
        "stock": 15,
        "disponible": True,
    },
    {
        "nombre": "latte de vainilla",
        "descripcion": "Café con leche y un toque de vainilla.",
        "precio": 8.50,
        "stock": 0,
        "disponible": True,
    },
    {
        "nombre": "croissant de mantequilla",
        "descripcion": "Hojaldre artesanal recién horneado.",
        "precio": 4.20,
        "stock": 30,
        "disponible": True,
    },
    {
        "nombre": "torta de chocolate",
        "descripcion": "Porción de torta húmeda con ganache.",
        "precio": 9.00,
        "stock": 8,
        "disponible": True,
    },
    {
        "nombre": "jugo de naranja",
        "descripcion": "Jugo natural exprimido al momento.",
        "precio": 6.00,
        "stock": 12,
        "disponible": False,
    },  # No disponible
]

for data in productos:
    Producto.objects.create(**data)

print(f"Se insertaron {Producto.objects.count()} productos.")
