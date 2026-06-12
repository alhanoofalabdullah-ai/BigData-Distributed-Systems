SELECT

category,

COUNT(*) AS products

FROM dim_products

GROUP BY category;
