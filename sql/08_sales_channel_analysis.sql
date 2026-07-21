SELECT
    o.sales_channel,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(
        oi.quantity *
        oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ) AS revenue
FROM orders AS o
JOIN order_items AS oi
ON o.order_id = oi.order_id
GROUP BY
    o.sales_channel
ORDER BY
    revenue DESC;