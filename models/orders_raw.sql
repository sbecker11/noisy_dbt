-- orders_raw.sql

CREATE TABLE raw_data.orders_raw (
    order_id INT,
    customer_id INT,
    order_date DATE,
    order_total DECIMAL(10, 2),
    -- other columns...
);
