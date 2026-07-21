-- ==========================================================
-- Project : Revenue Leak Detection & Growth Opportunity Analysis
-- Author  : Biswajeet Ojha
-- Purpose : Create all database tables (SQLite) with data-quality checks
-- ==========================================================

-- PRAGMA foreign_keys = ON;


-- ===========================
-- Customers
-- ===========================
CREATE TABLE customers (
    customer_id   INTEGER PRIMARY KEY,
    customer_name TEXT    NOT NULL,
    gender        TEXT    NOT NULL
        CHECK (gender IN ('Male', 'Female','Other')),
    age           INTEGER NOT NULL
        CHECK (age BETWEEN 18 AND 80),
    city          TEXT    NOT NULL,
    region        TEXT    NOT NULL,
    segment       TEXT    NOT NULL
        CHECK (segment IN ('Retail', 'Wholesale','Distributor')),
    signup_date   DATE    NOT NULL
);


-- ===========================
-- Products
-- ===========================
CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY,
    product_name TEXT    NOT NULL,
    category     TEXT    NOT NULL,
    brand        TEXT    NOT NULL,
    cost_price   REAL    NOT NULL
        CHECK (cost_price >= 0),
    list_price   REAL    NOT NULL
        CHECK (list_price >= 0)
);


-- ===========================
-- Orders
-- ===========================
CREATE TABLE orders (
    order_id      INTEGER PRIMARY KEY,
    customer_id   INTEGER NOT NULL,
    order_date    DATE    NOT NULL,
    status        TEXT    NOT NULL
        CHECK (status IN ('Completed', 'Cancelled', 'Returned')),
    sales_channel TEXT    NOT NULL
        CHECK (sales_channel IN ('Website', 'Mobile App', 'Marketplace')),
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- ===========================
-- Order Items
-- ===========================
CREATE TABLE order_items (
    order_item_id    INTEGER PRIMARY KEY,
    order_id         INTEGER NOT NULL,
    product_id       INTEGER NOT NULL,
    quantity         INTEGER NOT NULL
        CHECK (quantity > 0),
    unit_price       REAL    NOT NULL
        CHECK (unit_price >= 0),
    discount_percent REAL    NOT NULL
        CHECK (discount_percent BETWEEN 0 AND 100),
    discount_type    TEXT    NOT NULL
        CHECK (discount_type IN (
            'No Discount',
            'Coupon',
            'Flash Sale',
            'Festival Sale',
            'Membership'
        )),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);


-- ===========================
-- Delivery
-- ===========================
CREATE TABLE delivery (
    delivery_id     INTEGER PRIMARY KEY,
    order_id        INTEGER NOT NULL,
    dispatch_date   DATE    NOT NULL,
    delivery_date   DATE    NOT NULL,
    courier         TEXT    NOT NULL,
    delivery_status TEXT    NOT NULL
        CHECK (delivery_status IN ('Delivered', 'Delayed')),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);