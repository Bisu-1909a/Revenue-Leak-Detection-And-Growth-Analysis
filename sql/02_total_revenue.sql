SELECT
    SUM(
        quantity * unit_price *
        (1 - discount_percent / 100.0)
    ) AS total_revenue
FROM order_items;