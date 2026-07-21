import csv
import random
from datetime import datetime, timedelta


OUTPUT_FILE = "data/raw/delivery.csv"
TOTAL_ORDERS = 500


# -------------------------
# Couriers
# -------------------------
COURIERS = [
    "Blue Dart",
    "Delhivery",
    "DTDC",
    "Ekart",
    "India Post",
    "XpressBees"
]

COURIER_WEIGHTS = [
    20,
    25,
    15,
    15,
    10,
    15
]


# -------------------------
# Delivery status
# -------------------------
DELIVERY_STATUS = [
    "Delivered",
    "Delayed"
]

DELIVERY_STATUS_WEIGHTS = [
    92,   # Delivered
    8     # Delayed
]


def generate_delivery_status() -> str:
    """
    Generate delivery status using
    realistic business probabilities.
    """
    return random.choices(
        DELIVERY_STATUS,
        weights=DELIVERY_STATUS_WEIGHTS,
        k=1
    )[0]


def generate_courier() -> str:
    """
    Generate a courier using
    realistic business distribution.
    """
    return random.choices(
        COURIERS,
        weights=COURIER_WEIGHTS,
        k=1
    )[0]


# -------------------------
# Dates
# -------------------------
def generate_dispatch_date() -> str:
    """
    Generate a dispatch date between
    2024-01-01 and 2025-12-31.
    """
    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)

    total_days = (end - start).days
    random_days = random.randint(0, total_days)

    dispatch_date = start + timedelta(days=random_days)
    return dispatch_date.strftime("%Y-%m-%d")


def generate_delivery_date(
    dispatch_date: str,
    delivery_status: str
) -> str:
    """
    Generate a delivery date after
    the dispatch date.
    Delivered: 1–7 days later
    Delayed:   8–15 days later
    """
    dispatch = datetime.strptime(
        dispatch_date,
        "%Y-%m-%d"
    )

    if delivery_status == "Delivered":
        days = random.randint(1, 7)
    else:  # "Delayed"
        days = random.randint(8, 15)

    delivery = dispatch + timedelta(days=days)
    return delivery.strftime("%Y-%m-%d")


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

        # Header matching SQL table: delivery(...)
        writer.writerow([
            "delivery_id",
            "order_id",
            "dispatch_date",
            "delivery_date",
            "courier",
            "delivery_status"
        ])

        for delivery_id in range(1, TOTAL_ORDERS + 1):
            order_id = delivery_id

            dispatch_date = generate_dispatch_date()
            delivery_status = generate_delivery_status()
            delivery_date = generate_delivery_date(
                dispatch_date,
                delivery_status
            )
            courier = generate_courier()

            writer.writerow([
                delivery_id,
                order_id,
                dispatch_date,
                delivery_date,
                courier,
                delivery_status
            ])

    print(f"{TOTAL_ORDERS} deliveries generated successfully!")


if __name__ == "__main__":
    main()
    
