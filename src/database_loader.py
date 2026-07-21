import sqlite3
import csv


DATABASE_FILE = "data/database/retail_sales.db"
RAW_DATA_FOLDER = "data/raw"


def create_database_connection():
    """
    Create and return a connection
    to the SQLite database.
    """
    connection = sqlite3.connect(
        DATABASE_FILE
    )
    return connection


def create_customers_table(connection):
    """
    Create the customers table
    if it does not already exist.
    """
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id   INTEGER PRIMARY KEY,
            customer_name TEXT    NOT NULL,
            gender        TEXT    NOT NULL,
            age           INTEGER NOT NULL,
            city          TEXT    NOT NULL,
            region        TEXT    NOT NULL,
            segment       TEXT    NOT NULL,
            signup_date   TEXT    NOT NULL
        );
    """)

    connection.commit()


def clear_customers_table(connection):
    """
    Remove all existing records
    from the customers table.
    """
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM customers;
    """)

    connection.commit()


def load_customers_data(connection):
    """
    Load customers.csv into the customers table.
    """
    cursor = connection.cursor()

    with open(
        f"{RAW_DATA_FOLDER}/customers.csv",
        mode="r",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO customers (
                    customer_id,
                    customer_name,
                    gender,
                    age,
                    city,
                    region,
                    segment,
                    signup_date
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                int(row["customer_id"]),
                row["customer_name"],
                row["gender"],
                int(row["age"]),
                row["city"],
                row["region"],
                row["segment"],
                row["signup_date"]
            ))

    connection.commit()


def create_products_table(connection):
    """
    Create the products table
    if it does not already exist.
    """
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id   INTEGER PRIMARY KEY,
            product_name TEXT    NOT NULL,
            category     TEXT    NOT NULL,
            brand        TEXT    NOT NULL,
            cost_price   REAL    NOT NULL,
            list_price   REAL    NOT NULL
        );
    """)

    connection.commit()


def clear_products_table(connection):
    """
    Remove all existing records
    from the products table.
    """
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM products;
    """)

    connection.commit()


def load_products_data(connection):
    """
    Load products.csv into the products table.
    """
    cursor = connection.cursor()

    with open(
        f"{RAW_DATA_FOLDER}/products.csv",
        mode="r",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO products (
                    product_id,
                    product_name,
                    category,
                    brand,
                    cost_price,
                    list_price
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                int(row["product_id"]),
                row["product_name"],
                row["category"],
                row["brand"],
                float(row["cost_price"]),
                float(row["list_price"])
            ))

    connection.commit()


def create_orders_table(connection):
    """
    Create the orders table
    if it does not already exist.
    """
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id      INTEGER PRIMARY KEY,
            customer_id   INTEGER NOT NULL,
            order_date    TEXT    NOT NULL,
            status        TEXT    NOT NULL,
            sales_channel TEXT    NOT NULL,
            FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id)
        );
    """)

    connection.commit()


def clear_orders_table(connection):
    """
    Remove all existing records
    from the orders table.
    """
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM orders;
    """)

    connection.commit()


def load_orders_data(connection):
    """
    Load orders.csv into the orders table.
    """
    cursor = connection.cursor()

    with open(
        f"{RAW_DATA_FOLDER}/orders.csv",
        mode="r",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO orders (
                    order_id,
                    customer_id,
                    order_date,
                    status,
                    sales_channel
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                int(row["order_id"]),
                int(row["customer_id"]),
                row["order_date"],
                row["status"],
                row["sales_channel"]
            ))

    connection.commit()


def create_order_items_table(connection):
    """
    Create the order_items table
    if it does not already exist.
    """
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id    INTEGER PRIMARY KEY,
            order_id         INTEGER NOT NULL,
            product_id       INTEGER NOT NULL,
            quantity         INTEGER NOT NULL,
            unit_price       REAL    NOT NULL,
            discount_percent INTEGER NOT NULL,
            discount_type    TEXT    NOT NULL,
            FOREIGN KEY (order_id)
                REFERENCES orders(order_id),
            FOREIGN KEY (product_id)
                REFERENCES products(product_id)
        );
    """)

    connection.commit()


def clear_order_items_table(connection):
    """
    Remove all existing records
    from the order_items table.
    """
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM order_items;
    """)

    connection.commit()


def load_order_items_data(connection):
    """
    Load order_items.csv into the order_items table.
    """
    cursor = connection.cursor()

    with open(
        f"{RAW_DATA_FOLDER}/order_items.csv",
        mode="r",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO order_items (
                    order_item_id,
                    order_id,
                    product_id,
                    quantity,
                    unit_price,
                    discount_percent,
                    discount_type
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                int(row["order_item_id"]),
                int(row["order_id"]),
                int(row["product_id"]),
                int(row["quantity"]),
                float(row["unit_price"]),
                int(row["discount_percent"]),
                row["discount_type"]
            ))

    connection.commit()


def create_delivery_table(connection):
    """
    Create the delivery table
    if it does not already exist.
    """
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS delivery (
            delivery_id     INTEGER PRIMARY KEY,
            order_id        INTEGER NOT NULL,
            courier         TEXT    NOT NULL,
            dispatch_date   TEXT    NOT NULL,
            delivery_date   TEXT    NOT NULL,
            delivery_status TEXT    NOT NULL,
            FOREIGN KEY (order_id)
                REFERENCES orders(order_id)
        );
    """)

    connection.commit()


def clear_delivery_table(connection):
    """
    Remove all existing records
    from the delivery table.
    """
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM delivery;
    """)

    connection.commit()


def load_delivery_data(connection):
    """
    Load delivery.csv into the delivery table.
    """
    cursor = connection.cursor()

    with open(
        f"{RAW_DATA_FOLDER}/delivery.csv",
        mode="r",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO delivery (
                    delivery_id,
                    order_id,
                    courier,
                    dispatch_date,
                    delivery_date,
                    delivery_status
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                int(row["delivery_id"]),
                int(row["order_id"]),
                row["courier"],
                row["dispatch_date"],
                row["delivery_date"],
                row["delivery_status"]
            ))

    connection.commit()


def main():
    connection = create_database_connection()

    # Create tables
    create_customers_table(connection)
    create_products_table(connection)
    create_orders_table(connection)
    create_order_items_table(connection)
    create_delivery_table(connection)

    # Clear old data
    clear_customers_table(connection)
    clear_products_table(connection)
    clear_orders_table(connection)
    clear_order_items_table(connection)
    clear_delivery_table(connection)

    # Load fresh data
    load_customers_data(connection)
    load_products_data(connection)
    load_orders_data(connection)
    load_order_items_data(connection)
    load_delivery_data(connection)

    cursor = connection.cursor()

    # Verify customers
    cursor.execute("""
        SELECT COUNT(*)
        FROM customers
    """)
    total_customers = cursor.fetchone()[0]
    print(f"Customers loaded: {total_customers}")

    # Verify products
    cursor.execute("""
        SELECT COUNT(*)
        FROM products
    """)
    total_products = cursor.fetchone()[0]
    print(f"Products loaded: {total_products}")

    # Verify orders
    cursor.execute("""
        SELECT COUNT(*)
        FROM orders
    """)
    total_orders = cursor.fetchone()[0]
    print(f"Orders loaded: {total_orders}")

    # Verify order items
    cursor.execute("""
        SELECT COUNT(*)
        FROM order_items
    """)
    total_order_items = cursor.fetchone()[0]
    print(f"Order items loaded: {total_order_items}")

    # Verify delivery
    cursor.execute("""
        SELECT COUNT(*)
        FROM delivery
    """)
    total_delivery = cursor.fetchone()[0]
    print(f"Delivery records loaded: {total_delivery}")

    connection.close()


if __name__ == "__main__":
    main()
