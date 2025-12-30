{{ config(materialized='view') }}

select
    id as event_id,
    user_id,
    session_id,
    created_at as event_timestamp,
    traffic_source,
    event_type
from `bigquery-public-data.thelook_ecommerce.events`
where user_id is not null
