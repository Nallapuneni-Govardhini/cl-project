{{ config(materialized='view') }}

select
    order_id,
    user_id,
    created_at as order_timestamp,
    status,
    num_of_item
from `bigquery-public-data.thelook_ecommerce.orders`
where status = 'Complete'
