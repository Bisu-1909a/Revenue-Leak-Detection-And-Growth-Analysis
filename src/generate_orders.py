import csv
import random
from datetime import datetime, timedelta


OUTPUT_FILE = "data/raw/orders.csv"
TOTAL_ORDERS = 500

# -------------------------
# Customer groups
# -------------------------
LOYAL_CUSTOMERS = range(1, 21)      # 1–20
REGULAR_CUSTOMERS = range(21, 71)   # 21–70
OCCASIONAL_CUSTOMERS = range(71, 101)  # 71–100

CUSTOMER_GROUPS = [
    LOYAL_CUSTOMERS,
    REGULAR_CUSTOMERS,
    OCCASIONAL_CUSTOMERS
]

CUSTOMER_GROUP_WEIGHTS = [
    40,   # Loyal
    45,   # Regular
    15    # Occasional
]


# -------------------------
# Order status & channels
# -------------------------
ORDER_STATUS = [
    "Completed",
    "Cancelled",
    "Returned"
]

ORDER_STATUS_WEIGHTS = [
    88,   # Completed
    7,    # Cancelled
    5     # Returned
]

SALES_CHANNELS = [
    "Website",
    "Mobile App",
    "Marketplace"
]

SALES_CHANNEL_WEIGHTS = [
    45,   # Website
    35,   # Mobile App
    20    # Marketplace
]


# -------------------------
# Helper Functions
# -------------------------
def generate_customer_id() -> int:
    """
    Generate a customer ID using realistic purchasing behavior.
    Loyal customers appear more frequently than occasional ones.
    """
    customer_group = random.choices(
        CUSTOMER_GROUPS,
        weights=CUSTOMER_GROUP_WEIGHTS,
        k=1
    )[0]

    return random.choice(tuple(customer_group))


def generate_order_date() -> str:
    """
    Generate a random order date between
    2024-01-01 and 2025-12-31 (YYYY-MM-DD).
    """
    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)

    total_days = (end - start).days
    random_days = random.randint(0, total_days)

    order_date = start + timedelta(days=random_days)
    return order_date.strftime("%Y-%m-%d")


def generate_order_status() -> str:
    """
    Generate an order status using
    realistic business probabilities.
    """
    return random.choices(
        ORDER_STATUS,
        weights=ORDER_STATUS_WEIGHTS,
        k=1
    )[0]


def generate_sales_channel() -> str:
    """
    Generate a sales channel using
    business distribution.
    """
    return random.choices(
        SALES_CHANNELS,
        weights=SALES_CHANNEL_WEIGHTS,
        k=1
    )[0]


# -------------------------
# Main
# -------------------------
def main():
    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        # Header must match SQL table: orders(...)
        writer.writerow([
            "order_id",
            "customer_id",
            "order_date",
            "status",
            "sales_channel"
        ])

        for order_id in range(1, TOTAL_ORDERS + 1):
            customer_id = generate_customer_id()
            order_date = generate_order_date()
            status = generate_order_status()
            sales_channel = generate_sales_channel()

            writer.writerow([
                order_id,
                customer_id,
                order_date,
                status,
                sales_channel
            ])

    print(f"{TOTAL_ORDERS} orders generated successfully!")


if __name__ == "__main__":
    main()
    
