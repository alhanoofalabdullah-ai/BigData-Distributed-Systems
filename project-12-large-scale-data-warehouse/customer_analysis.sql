SELECT

customer_segment,

COUNT(*) AS total_customers

FROM dim_customers

GROUP BY customer_segment;
