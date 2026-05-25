{{
    config(
        materialized='table'
    )
}}

with green_tripdata as (
    select *,
    'Green' as service_type
    from {{ ref('stg_green_tripdata') }}
),
yellow_tripdata as (
    select *,
    'Yellow' as service_type
    from {{ ref('stg_yellow_tripdata') }}
),
trips_unioned as (
    select  
        unique_row_id,
        filename,
        vendor_id,
        pickup_datetime,  -- lpep = Licensed Passenger Enhancement Program (green taxis)
        dropoff_datetime,
        store_and_fwd_flag,
        rate_code_id,
        pickup_location_id,
        dropoff_location_id,
        passenger_count,
        trip_distance,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        improvement_surcharge,
        total_amount,
        trip_type,
        service_type,
        payment_type,
        congestion_surcharge,
    from green_tripdata
    union all
    select  
        unique_row_id,
        filename,
        vendor_id,
        pickup_datetime,  -- lpep = Licensed Passenger Enhancement Program (green taxis)
        dropoff_datetime,
        store_and_fwd_flag,
        rate_code_id,
        pickup_location_id,
        dropoff_location_id,
        passenger_count,
        trip_distance,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        improvement_surcharge,
        total_amount,
        trip_type,
        service_type,
        payment_type,
        congestion_surcharge,
    from yellow_tripdata
),
dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)

select
    t.*,

    -- pickup zone columns
    pickup_zone.location_id as pickup_location_id_dim,
    pickup_zone.borough as pickup_borough,
    pickup_zone.zone as pickup_zone_name,

    -- dropoff zone columns
    dropoff_zone.location_id as dropoff_location_id_dim,
    dropoff_zone.borough as dropoff_borough,
    dropoff_zone.zone as dropoff_zone_name

from trips_unioned t

inner join dim_zones as pickup_zone
    on t.pickup_location_id = pickup_zone.location_id

inner join dim_zones as dropoff_zone
    on t.dropoff_location_id = dropoff_zone.location_id