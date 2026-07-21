SELECT
    p.product_name,
    SUM(
        oi.quantity *
        oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ) AS revenue
FROM order_items AS oi
JOIN products AS p
ON oi.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    revenue DESC;