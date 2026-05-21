with 

source as (

    select * from {{ source('staging', 'yellow_tripdata') }}

),

renamed as (

    select
        unique_row_id,
        filename,
        cast(vendorid as integer) as vendor_id,
        cast(tpep_pickup_datetime as timestamp) as pickup_datetime, 
        cast(tpep_dropoff_datetime as timestamp) as dropoff_datetime,               
        passenger_count,
        trip_distance,
        cast(ratecodeid as integer) as rate_code_id,
        store_and_fwd_flag,
        cast(pulocationid as integer) as pickup_location_id,
        cast(dolocationid as integer) as dropoff_location_id,
        payment_type,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        Null as ehail_fee,
        improvement_surcharge,
        total_amount,
        Null as trip_type,
        congestion_surcharge
        

    from source

)

select * from renamed