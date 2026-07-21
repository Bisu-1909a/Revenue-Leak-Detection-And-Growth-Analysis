import csv
import random


OUTPUT_FILE = "data/raw/order_items.csv"

TOTAL_ORDERS = 500          # Must match orders.csv
TOTAL_PRODUCTS = 50
MAX_ITEMS_PER_ORDER = 4


# -------------------------
# Product price loader
# -------------------------
def load_product_prices() -> dict[int, float]:
    """
    Load product prices from products.csv.
    Returns:
        {product_id: list_price}
    """
    with open(
        "data/raw/products.csv",
        mode="r",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        product_prices = {}

        for row in reader:
            product_id = int(row["product_id"])
            list_price = float(row["list_price"])
            product_prices[product_id] = list_price

    return product_prices


# -------------------------
# Helper Functions
# -------------------------
def generate_product_ids_for_order(number_of_items: int) -> list[int]:
    """
    Generate a list of unique product IDs for a single order.
    """
    max_items = min(number_of_items, TOTAL_PRODUCTS)
    return random.sample(
        range(1, TOTAL_PRODUCTS + 1),
        k=max_items
    )


QUANTITIES = [1, 2, 3, 4, 5]
QUANTITY_WEIGHTS = [50, 25, 15, 7, 3]


def generate_quantity() -> int:
    """
    Generate a realistic purchase quantity.
    """
    return random.choices(
        QUANTITIES,
        weights=QUANTITY_WEIGHTS,
        k=1
    )[0]


DISCOUNT_PERCENTAGES = [
    0,
    5,
    10,
    15,
    20,
    25,
    30
]

DISCOUNT_PERCENTAGE_WEIGHTS = [
    45,  # No discount
    15,
    18,
    10,
    7,
    3,
    2
]


def generate_discount_percent() -> int:
    """
    Generate a realistic discount percentage.
    """
    return random.choices(
        DISCOUNT_PERCENTAGES,
        weights=DISCOUNT_PERCENTAGE_WEIGHTS,
        k=1
    )[0]


def generate_discount_type(discount_percent: int) -> str:
    """
    Generate discount type based on discount percentage.
    """
    if discount_percent == 0:
        return "No Discount"
    elif discount_percent <= 10:
        return "Coupon"
    elif discount_percent <= 20:
        return "Festival Sale"
    else:
        return "Membership"


# -------------------------
# Main
# -------------------------
def main():
    # Step 1: load product prices into a lookup dictionary
    product_prices = load_product_prices()

    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as f:
        writer = csv.writer(f)

        # CSV header must match order_items table
        writer.writerow([
            "order_item_id",
            "order_id",
            "product_id",
            "quantity",
            "unit_price",
            "discount_percent",
            "discount_type"
        ])

        order_item_id = 1

        # Loop through every order
        for order_id in range(1, TOTAL_ORDERS + 1):
            # Decide how many items this order has
            number_of_items = random.randint(1, MAX_ITEMS_PER_ORDER)

            # Pick unique product_ids for this order
            product_ids = generate_product_ids_for_order(number_of_items)

            for product_id in product_ids:
                quantity = generate_quantity()

                # Step 2: use real list_price from products.csv
                unit_price = product_prices[product_id]

                discount_percent = generate_discount_percent()
                discount_type = generate_discount_type(discount_percent)

                writer.writerow([
                    order_item_id,
                    order_id,
                    product_id,
                    quantity,
                    unit_price,
                    discount_percent,
                    discount_type
                ])

                order_item_id += 1

    print(f"{order_item_id - 1} order items generated successfully!")


if __name__ == "__main__":
    main()
    
