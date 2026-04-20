select
    id as organization_id,
    name as organization_name,
    address,
    city,
    state,
    zip,
    lat as latitude,
    lon as longitude,
    phone,
    revenue,
    utilization
from {{ source('raw_healthcare', 'organizations') }}