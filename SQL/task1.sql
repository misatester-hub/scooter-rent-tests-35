SELECT c.login, COUNT(o.id) AS delivery_orders_count
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;
