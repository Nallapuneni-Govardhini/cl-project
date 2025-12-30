{{ config(materialized='view') }}

select
    id as user_id,
    traffic_source as user_first_source,
    created_at as user_created_at
from `bigquery-public-data.thelook_ecommerce.users`
