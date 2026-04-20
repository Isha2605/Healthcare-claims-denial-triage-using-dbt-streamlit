select
    c.claim_id,
    c.patient_id,
    c.provider_id,
    c.department_id,
    c.patient_department_id,
    c.primary_patient_insurance_id,
    c.secondary_patient_insurance_id,
    c.appointment_id,
    c.service_date,
    c.current_illness_date,

    c.status_primary,
    c.status_secondary,
    c.status_patient,

    c.outstanding_primary,
    c.outstanding_secondary,
    c.outstanding_patient,

    c.diagnosis_1,
    c.diagnosis_2,
    c.diagnosis_3,
    c.diagnosis_4,
    c.diagnosis_5,
    c.diagnosis_6,
    c.diagnosis_7,
    c.diagnosis_8,

    c.referring_provider_id,
    c.supervising_provider_id,

    c.last_billed_date_primary,
    c.last_billed_date_secondary,
    c.last_billed_date_patient,

    f.transaction_count,
    f.total_transaction_amount,
    f.total_payments,
    f.total_adjustments,
    f.total_transfers,
    f.latest_outstanding,
    f.first_transaction_date,
    f.last_transaction_date,
    f.transaction_type_count,
    f.procedure_code_count,

    p.birth_date,
    p.death_date,
    p.gender,
    p.race,
    p.ethnicity,
    p.marital_status,
    p.city as patient_city,
    p.state as patient_state,
    p.county as patient_county,
    p.zip as patient_zip,
    p.healthcare_expenses,
    p.healthcare_coverage,
    p.income,

    pr.provider_name,
    pr.specialty,
    pr.gender as provider_gender,
    pr.organization_id,

    o.organization_name,
    o.city as organization_city,
    o.state as organization_state,
    o.revenue as organization_revenue,
    o.utilization as organization_utilization,

    coalesce(c.outstanding_primary, 0)
      + coalesce(c.outstanding_secondary, 0)
      + coalesce(c.outstanding_patient, 0) as claim_outstanding_total,

    case
        when coalesce(f.latest_outstanding, 0) > 1000 then 'high'
        when coalesce(f.latest_outstanding, 0) > 250 then 'medium'
        else 'low'
    end as financial_priority_bucket

from {{ ref('stg_claims') }} c

left join {{ ref('int_claim_financials') }} f
    on c.claim_id = f.claim_id

left join {{ ref('stg_patients') }} p
    on c.patient_id = p.patient_id

left join {{ ref('stg_providers') }} pr
    on c.provider_id = pr.provider_id

left join {{ ref('stg_organizations') }} o
    on pr.organization_id = o.organization_id