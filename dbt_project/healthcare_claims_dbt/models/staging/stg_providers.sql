select
    id as provider_id,
    organization as organization_id,
    name as provider_name,
    gender,
    speciality as specialty,
    address,
    city,
    state,
    zip,
    lat as latitude,
    lon as longitude,
    encounters as encounter_count,
    procedures as procedure_count
from {{ source('raw_healthcare', 'providers') }}