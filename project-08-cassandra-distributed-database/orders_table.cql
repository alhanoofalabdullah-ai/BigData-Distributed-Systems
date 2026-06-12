CREATE TABLE orders (

order_id UUID PRIMARY KEY,

customer_id UUID,

order_date TIMESTAMP,

amount DECIMAL,

status TEXT

);
