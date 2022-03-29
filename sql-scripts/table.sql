CREATE TABLE IF NOT EXISTS 'trip'
(
    VendorID INT NOT NULL ,
    tpep_pickup_datetime DATE NOT NULL,
    tpep_dropoff_datetime DATE NOT NULL,
    passenger_count INT NOT NULL,
    trip_distance FLOAT NOT NULL,
    RatecodeID INT NOT NOT NULL,
    store_and_fwd_flag VARCHAR (20) NOT NULL,
    PULocationID INT NOT NULL,
    DOLocationID INT NOT NULL,
    payment_type INT NOT NULL,
    fare_amount INT NOT NULL,
    extra INT NOT NULL,
    mta_tax FLOAT NOT NULL,
    tip_amount INT NOT NULL,
    tolls_amount INT  NOT NULL,
    improvement_surcharge FLOAT NOT NULL,
    total_amount FLOAT NOT NULL,
    congestion_surcharge FLOAT NOT NULL,

);