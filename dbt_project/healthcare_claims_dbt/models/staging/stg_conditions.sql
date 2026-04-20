select
    start as condition_start,
    stop as condition_stop,
    patient as patient_id,
    encounter as encounter_id,
    system as condition_system,
    code as condition_code,
    description as condition_description
from {{ source('raw_healthcare', 'conditions') }}