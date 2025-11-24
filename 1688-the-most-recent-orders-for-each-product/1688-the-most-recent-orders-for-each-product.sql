SELECT 
    DISTINCT p.product_name,
    p.product_id,
    o.order_id,
    o.order_date
FROM 
    Products p 
JOIN 
    Orders o
ON 
    p.product_id = o.product_id
JOIN
    (
    SELECT 
        DISTINCT product_id, 
        MAX(order_date) AS order_date
    FROM 
        Orders
    GROUP BY 1
    )a
ON 
    o.product_id = a.product_id
AND 
    o.order_date = a.order_date
ORDER BY p.product_name,
    p.product_id,
    o.order_id