from functools import lru_cache

from .schema import Customer, Order, Product

CustomerStorageType = dict[int, Customer]
OrdersStorageType = dict[int, Order]
ProductsStorageType = dict[int, Product]

CUSTOMERS: CustomerStorageType = {}
ORDERS: OrdersStorageType = {
    0: Order(
        customer_id=[0],
        order_items=[0, 1, 2],
        order_id=0,
        price=11.11
    ),
    1: Order(
        customer_id=[1],
        order_items=[3, 4, 5],
        order_id=1,
        price=11.11
    ),
}
PRODUCTS: ProductsStorageType = {
    0: Product(name="prod1", price=12.99, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt pellentesque suscipit", id=0),
    1: Product(name="prod2", price=10.99, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt pellentesque suscipit", id=1),
    2: Product(name="prod3", price=15.99, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt pellentesque suscipit", id=2),
    3: Product(name="prod4", price=17.99, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt pellentesque suscipit", id=3),
    4: Product(name="prod5", price=80.99, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt pellentesque suscipit", id=4),
    5: Product(name="prod6", price=66.99, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tincidunt pellentesque suscipit", id=5),
}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS


@lru_cache(maxsize=1)
def get_orders_storage() -> OrdersStorageType:
    return ORDERS


@lru_cache(maxsize=1)
def get_products_storage() -> ProductsStorageType:
    return PRODUCTS
