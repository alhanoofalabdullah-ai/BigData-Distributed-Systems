SELECT

region_name,

COUNT(*) AS sales_count

FROM dim_region

GROUP BY region_name;
