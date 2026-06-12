CREATE TABLE fact_sales (

sales_id SERIAL PRIMARY KEY,

customer_id INT,

product_id INT,

date_id INT,

region_id INT,

quantity INT,

revenue DECIMAL(12,2)

);
