select
    start as procedure_start,
    stop as procedure_stop,
    patient as patient_id,
    encounter as encounter_id,
    system as procedure_system,
    code as procedure_code,
    description as procedure_description,
    base_cost,
    reasoncode as reason_code,
    reasondescription as reason_description
from {{ source('raw_healthcare', 'procedures') }}