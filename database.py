import json
from pathlib import Path

from models import Product

DB_FILE = Path(__file__).with_name("products.json")


def seed_products() -> list[Product]:
    return [
        Product(
            id=1,
            name="Laptop",
            price=1200.00,
            description="15-inch developer laptop",
            quantity=10,
        ),
        Product(
            id=2,
            name="Mechanical Keyboard",
            price=150.00,
            description="Backlit mechanical keyboard",
            quantity=25,
        ),
        Product(
            id=3,
            name="Wireless Mouse",
            price=60.00,
            description="Ergonomic wireless mouse",
            quantity=40,
        ),
        Product(
            id=4,
            name="Monitor",
            price=300.00,
            description="27-inch 4K monitor",
            quantity=15,
        ),
        Product(
            id=5,
            name="USB-C Dock",
            price=180.00,
            description="Multi-port docking station",
            quantity=20,
        ),
    ]


def save_products(products: list[Product]) -> None:
    payload = [product.model_dump() for product in products]
    DB_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def ensure_database_file() -> None:
    if not DB_FILE.exists():
        save_products(seed_products())


def get_products() -> list[Product]:
    ensure_database_file()
    raw_content = DB_FILE.read_text(encoding="utf-8")
    raw_products = json.loads(raw_content)
    return [Product(**item) for item in raw_products]


def get_product_by_id(product_id: int) -> Product | None:
    for product in get_products():
        if product.id == product_id:
            return product
    return None


def add_product(product: Product) -> Product:
    products = get_products()
    for existing_product in products:
        if existing_product.id == product.id:
            raise ValueError("Product ID already exists")
    products.append(product)
    save_products(products)
    return product


def update_product(product_id: int, product: Product) -> Product | None:
    products = get_products()

    if product.id != product_id:
        raise ValueError("Path product_id must match product.id")

    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products[index] = product
            save_products(products)
            return product

    return None


def delete_product(product_id: int) -> Product | None:
    products = get_products()

    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            deleted_product = products.pop(index)
            save_products(products)
            return deleted_product

    return None
