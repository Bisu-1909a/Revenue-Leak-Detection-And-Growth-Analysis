SELECT
    c.segment,
    SUM(
        oi.quantity *
        oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ) AS revenue
FROM order_items AS oi
JOIN orders AS o
ON oi.order_id = o.order_id
JOIN customers AS c
ON o.customer_id = c.customer_id
GROUP BY
    c.segment
ORDER BY
    revenue DESC;