{{ config(materialized='table') }}

with events as (
    select *
    from {{ ref('stg_events') }}
),

orders as (
    select *
    from {{ ref('stg_orders') }}
),

joined as (
    select
        o.order_id,
        o.user_id,
        o.order_timestamp,
        e.traffic_source,
        e.event_timestamp,
        row_number() over (
            partition by o.order_id
            order by e.event_timestamp asc
        ) as rn
    from orders o
    join events e
      on o.user_id = e.user_id
     and e.event_timestamp <= o.order_timestamp
)

select
    order_id,
    user_id,
    traffic_source as first_click_source,
    order_timestamp
from joined
where rn = 1
