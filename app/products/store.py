from copy import deepcopy
from decimal import Decimal


_INITIAL_PRODUCTS = [
    {"id": 1, "name": "Tarjeta gráfica Nova RTX 4060 8 GB", "category": "Componentes", "subcategory": "Tarjetas gráficas", "description": "GPU para juego y creación de contenido en resolución Full HD.", "price": Decimal("6999.00"), "stock_quantity": 8},
    {"id": 2, "name": "Tarjeta gráfica Nova RTX 4070 Super 12 GB", "category": "Componentes", "subcategory": "Tarjetas gráficas", "description": "GPU de rendimiento avanzado con 12 GB de memoria.", "price": Decimal("13999.00"), "stock_quantity": 4},
    {"id": 3, "name": "Tarjeta gráfica Radeon Pulse RX 7600 8 GB", "category": "Componentes", "subcategory": "Tarjetas gráficas", "description": "Tarjeta gráfica de gama media para equipos de escritorio.", "price": Decimal("5899.00"), "stock_quantity": 7},
    {"id": 4, "name": "Tarjeta gráfica Radeon Pulse RX 7800 XT 16 GB", "category": "Componentes", "subcategory": "Tarjetas gráficas", "description": "GPU con 16 GB para cargas gráficas de alta demanda.", "price": Decimal("11999.00"), "stock_quantity": 3},
    {"id": 5, "name": "PC Boreal Office i5 16 GB", "category": "Equipos", "subcategory": "Computadoras de escritorio", "description": "Equipo de oficina con 16 GB de RAM y SSD de 512 GB.", "price": Decimal("12499.00"), "stock_quantity": 5},
    {"id": 6, "name": "PC Boreal Creator Ryzen 7 32 GB", "category": "Equipos", "subcategory": "Computadoras de escritorio", "description": "Equipo para edición con 32 GB de RAM y SSD de 1 TB.", "price": Decimal("22999.00"), "stock_quantity": 2},
    {"id": 7, "name": "PC Boreal Gamer RTX 4060", "category": "Equipos", "subcategory": "Computadoras de escritorio", "description": "Equipo para juego con tarjeta gráfica dedicada y SSD de 1 TB.", "price": Decimal("24999.00"), "stock_quantity": 3},
    {"id": 8, "name": "Mini PC Boreal Compact N100", "category": "Equipos", "subcategory": "Computadoras de escritorio", "description": "Equipo compacto para navegación y tareas administrativas.", "price": Decimal("6499.00"), "stock_quantity": 9},
    {"id": 9, "name": "Laptop Andina 14 Core i5", "category": "Equipos", "subcategory": "Laptops", "description": "Portátil de 14 pulgadas con 16 GB de RAM y SSD de 512 GB.", "price": Decimal("13999.00"), "stock_quantity": 6},
    {"id": 10, "name": "Laptop Andina 15 Ryzen 7", "category": "Equipos", "subcategory": "Laptops", "description": "Portátil de 15 pulgadas para productividad y desarrollo.", "price": Decimal("16999.00"), "stock_quantity": 5},
    {"id": 11, "name": "Laptop Andina Pro 16 RTX 4060", "category": "Equipos", "subcategory": "Laptops", "description": "Portátil de alto rendimiento con gráficos dedicados.", "price": Decimal("29999.00"), "stock_quantity": 2},
    {"id": 12, "name": "Laptop Andina Air 13", "category": "Equipos", "subcategory": "Laptops", "description": "Portátil ligero con 16 GB de RAM y SSD de 512 GB.", "price": Decimal("15499.00"), "stock_quantity": 4},
    {"id": 13, "name": "Tarjeta madre Quetzal B550M", "category": "Componentes", "subcategory": "Tarjetas madre", "description": "Tarjeta micro-ATX compatible con procesadores AM4.", "price": Decimal("2199.00"), "stock_quantity": 10},
    {"id": 14, "name": "Tarjeta madre Quetzal B650 WiFi", "category": "Componentes", "subcategory": "Tarjetas madre", "description": "Tarjeta ATX para AM5 con red inalámbrica integrada.", "price": Decimal("3999.00"), "stock_quantity": 6},
    {"id": 15, "name": "Tarjeta madre Cóndor B760M", "category": "Componentes", "subcategory": "Tarjetas madre", "description": "Tarjeta micro-ATX para procesadores de escritorio compatibles.", "price": Decimal("2899.00"), "stock_quantity": 8},
    {"id": 16, "name": "Tarjeta madre Cóndor Z790 Pro", "category": "Componentes", "subcategory": "Tarjetas madre", "description": "Tarjeta ATX avanzada con múltiples ranuras de expansión.", "price": Decimal("5799.00"), "stock_quantity": 3},
    {"id": 17, "name": "Procesador Sierra Ryzen 5 7600", "category": "Componentes", "subcategory": "Procesadores", "description": "Procesador de seis núcleos para equipos de uso general.", "price": Decimal("4299.00"), "stock_quantity": 9},
    {"id": 18, "name": "Procesador Sierra Ryzen 7 7700", "category": "Componentes", "subcategory": "Procesadores", "description": "Procesador de ocho núcleos para productividad avanzada.", "price": Decimal("6599.00"), "stock_quantity": 5},
    {"id": 19, "name": "Procesador Horizonte Core i5 14400", "category": "Componentes", "subcategory": "Procesadores", "description": "Procesador de escritorio para productividad y juego.", "price": Decimal("4899.00"), "stock_quantity": 7},
    {"id": 20, "name": "Procesador Horizonte Core i7 14700", "category": "Componentes", "subcategory": "Procesadores", "description": "Procesador de alto rendimiento para cargas intensivas.", "price": Decimal("8299.00"), "stock_quantity": 4},
]

_products = deepcopy(_INITIAL_PRODUCTS)


def list_products():
    """Devuelve una copia superficial para evitar cambios desde la plantilla."""

    return [product.copy() for product in _products]


def add_product(*, name, category, subcategory, description, price, stock_quantity):
    product = {
        "id": max((item["id"] for item in _products), default=0) + 1,
        "name": name.strip(),
        "category": category.strip(),
        "subcategory": subcategory.strip(),
        "description": description.strip(),
        "price": Decimal(price).quantize(Decimal("0.01")),
        "stock_quantity": int(stock_quantity),
    }
    _products.append(product)
    return product.copy()
