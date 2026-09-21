-- Data Quality Validation Queries
-- These queries identify common data quality issues in the orders table.

-- 1. Find duplicate order IDs
SELECT
    order_id,
    COUNT(*) AS occurrence_count
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;


-- 2. Find missing or invalid amounts
SELECT *
FROM orders
WHERE amount IS NULL
   OR amount <= 0;


-- 3. Find unsupported currencies
SELECT *
FROM orders
WHERE currency NOT IN ('USD', 'EUR', 'ARS')
   OR currency IS NULL;


-- 4. Find invalid order statuses
SELECT *
FROM orders
WHERE status NOT IN ('completed', 'pending', 'cancelled')
   OR status IS NULL;


-- 5. Find missing required identifiers
SELECT *
FROM orders
WHERE order_id IS NULL
   OR customer_id IS NULL;


-- 6. Data quality summary
SELECT
    COUNT(*) AS total_orders,
    SUM(CASE WHEN amount IS NULL OR amount <= 0 THEN 1 ELSE 0 END)
        AS invalid_amounts,
    SUM(CASE WHEN currency NOT IN ('USD', 'EUR', 'ARS')
             OR currency IS NULL THEN 1 ELSE 0 END)
        AS invalid_currencies,
    SUM(CASE WHEN status NOT IN ('completed', 'pending', 'cancelled')
             OR status IS NULL THEN 1 ELSE 0 END)
        AS invalid_statuses
FROM orders;
