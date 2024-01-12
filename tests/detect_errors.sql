-- models/tests/detect_errors.sql

-- Test for Missing Data
with missing_data_counts as (
    select
        count(*) as missing_customer_id_count,
        count(*) as missing_order_timestamp_count
    from raw_data.orders
    where customer_id is null
        or order_timestamp is null
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Missing Data' as error_type,
    'Missing customer_id detected' as error_description
from missing_data_counts
where missing_customer_id_count > 0

union

select
    'Missing Data' as error_type,
    'Missing order_timestamp detected' as error_description
from missing_data_counts
where missing_order_timestamp_count > 0;


-- Test for Duplicate Records
with duplicate_counts as (
    select
        order_id,
        count(*) as count
    from raw_data.orders
    group by order_id
    having count(*) > 1
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Duplicate Records' as error_type,
    'Duplicate records detected' as error_description
from duplicate_counts;


-- Test for Data Type Mismatch
with data_type_mismatch_counts as (
    select
        'customer_id' as column_name,
        case when o.customer_id::string is distinct from c.customer_id then 1 else 0 end as mismatch_count
    from raw_data.orders o
    left join raw_data.customers c
    on o.customer_id = c.customer_id

    union

    select
        'product_id' as column_name,
        case when o.product_id::string is distinct from p.product_id then 1 else 0 end as mismatch_count
    from raw_data.orders o
    left join raw_data.products p
    on o.product_id = p.product_id
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Data Type Mismatch' as error_type,
    'Data type mismatches detected' as error_description
from data_type_mismatch_counts
where mismatch_count > 0;


-- Test for Invalid Date Format
with invalid_date_format_counts as (
    select
        count(*) as invalid_date_format_count
    from raw_data.orders
    where not order_timestamp::timestamp is not null
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Invalid Date Format' as error_type,
    'Invalid date formats detected' as error_description
from invalid_date_format_counts
where invalid_date_format_count > 0;


-- Test for Invalid Date
with invalid_date_counts as (
    select
        count(*) as invalid_date_count
    from raw_data.orders
    where try(order_timestamp::timestamp) is null
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Invalid Date' as error_type,
    'Invalid dates detected' as error_description
from invalid_date_counts
where invalid_date_count > 0;


-- Test for Outlier Quantity
with outlier_quantity_counts as (
    select
        count(*) as outlier_quantity_count
    from raw_data.orders
    where quantity::int > 20
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Outlier Quantity' as error_type,
    'Outlier quantities detected' as error_description
from outlier_quantity_counts
where outlier_quantity_count > 0;


-- Test for Outlier Price
with outlier_price_counts as (
    select
        count(*) as outlier_price_count
    from raw_data.orders
    where product_price::float > 100
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Outlier Price' as error_type,
    'Outlier prices detected' as error_description
from outlier_price_counts
where outlier_price_count > 0;


-- Test for Data Integrity Errors
with data_integrity_error_counts as (
    select
        count(*) as data_integrity_error_count
    from raw_data.orders o
    left join raw_data.customers c
    on o.customer_id = c.customer_id
    where c.customer_id is null
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'Data Integrity Errors' as error_type,
    'Data integrity errors detected' as error_description
from data_integrity_error_counts
where data_integrity_error_count > 0;


-- Test for String Encoding Errors
with encoding_error_counts as (
    select
        count(*) as encoding_error_count
    from raw_data.orders
    where length(customer_name) > 0
        and not convert_from(convert_to(customer_name, 'utf-8'), 'utf-8') = customer_name
)

insert into {{ ref('test_results') }} (
    error_type,
    error_description
)
select
    'String Encoding Errors' as error_type,
    'String encoding errors detected' as error_description
from encoding_error_counts
where encoding_error_count > 0;
