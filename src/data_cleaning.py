import pandas as pd


# ==========================================================
# Constants
# ==========================================================

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"


# ==========================================================
# Functions
# ==========================================================

def load_customers():
    """
    Load customers dataset.
    """
    return pd.read_csv(f"{RAW_FOLDER}/customers.csv")


def load_products():
    return pd.read_csv(f"{RAW_FOLDER}/products.csv")


def load_orders():
    return pd.read_csv(f"{RAW_FOLDER}/orders.csv")


def load_order_items():
    return pd.read_csv(f"{RAW_FOLDER}/order_items.csv")


def load_delivery():
    return pd.read_csv(f"{RAW_FOLDER}/delivery.csv")


def inspect_dataframe(df, dataset_name):
    """
    Display basic information
    about a dataset.
    """

    print("\n" + "=" * 60)
    print(f"Dataset : {dataset_name}")
    print("=" * 60)

    print(f"Rows      : {df.shape[0]}")
    print(f"Columns   : {df.shape[1]}")

    print(f"Missing Values : {df.isnull().sum().sum()}")

    print(f"Duplicate Rows : {df.duplicated().sum()}")

    print("=" * 60)


def clean_dataframe(df):
    """
    Clean a dataframe by removing duplicates
    and trimming whitespace from text columns.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean text columns
    for column in df.select_dtypes(include="object"):

        df[column] = df[column].str.strip()

    return df


def save_dataframe(df, filename):
    """
    Save a cleaned dataframe.
    """

    df.to_csv(
        f"{PROCESSED_FOLDER}/{filename}",
        index=False
    )

    print(f"✓ Saved: {filename}")


# ==========================================================
# Main
# ==========================================================

def main():

    customers = load_customers()
    products = load_products()
    orders = load_orders()
    order_items = load_order_items()
    delivery = load_delivery()

    inspect_dataframe(customers, "Customers")
    inspect_dataframe(products, "Products")
    inspect_dataframe(orders, "Orders")
    inspect_dataframe(order_items, "Order Items")
    inspect_dataframe(delivery, "Delivery")

    customers = clean_dataframe(customers)
    products = clean_dataframe(products)
    orders = clean_dataframe(orders)
    order_items = clean_dataframe(order_items)
    delivery = clean_dataframe(delivery)

    save_dataframe(customers, "customers.csv")
    save_dataframe(products, "products.csv")
    save_dataframe(orders, "orders.csv")
    save_dataframe(order_items, "order_items.csv")
    save_dataframe(delivery, "delivery.csv")

    print("\nFirst Five Records:\n")
    print(customers.head())


if __name__ == "__main__":
    main()