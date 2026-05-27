with 

source as (

    select * from {{ source('staging', 'green_tripdata') }}

),

renamed as (

    select
        unique_row_id,
        filename,
        cast(vendorid as integer) as vendor_id,
        cast(lpep_pickup_datetime as timestamp) as pickup_datetime,  
        cast(lpep_dropoff_datetime as timestamp) as dropoff_datetime,
        store_and_fwd_flag,
        {{ safe_cast('ratecodeid', 'integer') }} as rate_code_id,
        cast(pulocationid as integer) as pickup_location_id,
        cast(dolocationid as integer) as dropoff_location_id,
        passenger_count,
        trip_distance,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        ehail_fee,
        improvement_surcharge,
        total_amount,
        payment_type,
        cast(trip_type as integer) as trip_type,
        congestion_surcharge

    from source

)

select * from renamed