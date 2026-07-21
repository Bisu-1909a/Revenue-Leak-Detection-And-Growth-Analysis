import csv
import random


OUTPUT_FILE = "data/raw/products.csv"
TOTAL_PRODUCTS = 50


# -------------------------
# Product Catalog
# -------------------------
PRODUCT_CATALOG = {
    "Electronics": [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Smartwatch",
        "Earbuds",
        "Bluetooth Speaker",
        "Monitor",
        "Printer",
        "Webcam",
        "Router"
    ],

    "Home Appliances": [
        "Microwave Oven",
        "Mixer Grinder",
        "Vacuum Cleaner",
        "Air Purifier",
        "Electric Kettle",
        "Rice Cooker",
        "Induction Cooktop",
        "Ceiling Fan",
        "Water Purifier",
        "Washing Machine"
    ],

    "Furniture": [
        "Office Chair",
        "Study Table",
        "Bookshelf",
        "Computer Desk",
        "Sofa Chair",
        "Filing Cabinet",
        "Conference Table",
        "Wooden Stool",
        "TV Unit",
        "Wardrobe"
    ],

    "Office Supplies": [
        "Notebook",
        "Printer Paper",
        "Ink Cartridge",
        "Ball Pen Pack",
        "Sticky Notes",
        "Desk Organizer",
        "Whiteboard",
        "Marker Set",
        "Stapler",
        "File Folder"
    ],

    "Accessories": [
        "Mouse",
        "Keyboard",
        "Laptop Bag",
        "USB Drive",
        "Power Bank",
        "HDMI Cable",
        "Phone Charger",
        "Backpack",
        "Mouse Pad",
        "Webcam Stand"
    ]
}


# -------------------------
# Brands
# -------------------------
BRANDS = [
    "TechNova",
    "NexGen",
    "PrimeGear",
    "SmartTech",
    "UrbanLiving",
    "HomeEase",
    "OfficePro",
    "EliteHome",
    "ComfortPlus",
    "EcoWorks"
]


# -------------------------
# Category Pricing
# (cost_price range)
# -------------------------
CATEGORY_COST_RANGE = {
    "Electronics": (8000, 70000),
    "Home Appliances": (1500, 30000),
    "Furniture": (2000, 25000),
    "Office Supplies": (20, 3000),
    "Accessories": (100, 5000)
}


# -------------------------
# Helper Functions
# -------------------------
def generate_brand() -> str:
    """
    Generate a random brand from the predefined brand list.
    """
    return random.choice(BRANDS)


def generate_cost_price(category: str) -> float:
    """
    Generate a realistic cost price based on the product category.
    """
    minimum_price, maximum_price = CATEGORY_COST_RANGE[category]
    return round(
        random.uniform(minimum_price, maximum_price),
        2
    )


MARKUP_RANGE = {
    "Electronics": (10, 20),
    "Home Appliances": (20, 35),
    "Furniture": (25, 45),
    "Office Supplies": (40, 70),
    "Accessories": (50, 90)
}


def generate_list_price(
    category: str,
    cost_price: float
) -> float:
    """
    Generate the selling price using category-specific markup.
    """
    minimum_markup, maximum_markup = MARKUP_RANGE[category]

    markup_percent = random.uniform(
        minimum_markup,
        maximum_markup
    )

    list_price = cost_price * (1 + markup_percent / 100)
    return round(list_price, 2)


# -------------------------
# Main
# -------------------------
def main():
    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as f:
        writer = csv.writer(f)
        writer.writerow([
            "product_id",
            "product_name",
            "category",
            "brand",
            "cost_price",
            "list_price"
        ])

        product_id = 1
        for category, products in PRODUCT_CATALOG.items():
            for product_name in products:
                brand = generate_brand()
                cost_price = generate_cost_price(category)
                list_price = generate_list_price(category, cost_price)

                writer.writerow([
                    product_id,
                    product_name,
                    category,
                    brand,
                    cost_price,
                    list_price
                ])
                product_id += 1

    print(f"{product_id - 1} products generated successfully!")


if __name__ == "__main__":
    main()
    
