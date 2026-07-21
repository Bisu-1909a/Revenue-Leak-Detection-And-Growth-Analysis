SELECT
    discount_percent,
    COUNT(*) AS total_items_sold,
    SUM(
        quantity *
        unit_price *
        (1 - discount_percent / 100.0)
    ) AS revenue
FROM order_items
GROUP BY
    discount_percent
ORDER BY
    revenue DESC;