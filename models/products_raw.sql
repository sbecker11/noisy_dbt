-- products_raw.sql

CREATE TABLE raw_data.products_raw (
    product_id INT,
    product_name VARCHAR(255),
    product_description TEXT,
    product_price DECIMAL(10, 2),
    -- other columns...
);
