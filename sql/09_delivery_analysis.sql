SELECT
    courier,
    delivery_status,
    COUNT(*) AS total_orders
FROM delivery
GROUP BY
    courier,
    delivery_status
ORDER BY
    courier,
    delivery_status;