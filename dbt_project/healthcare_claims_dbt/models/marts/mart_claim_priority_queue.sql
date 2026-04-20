with base as (

    select
        claim_id,
        patient_id,
        provider_id,
        provider_name,
        specialty,
        organization_id,
        organization_name,
        patient_city,
        patient_state,
        service_date,
        status_primary,
        status_secondary,
        status_patient,
        claim_outstanding_total,
        latest_outstanding,
        transaction_count,
        total_transaction_amount,
        total_payments,
        total_adjustments,
        total_transfers,
        first_transaction_date,
        last_transaction_date,
        financial_priority_bucket
    from {{ ref('int_claim_enriched') }}

),

final as (

    select
        claim_id,
        patient_id,
        provider_id,
        provider_name,
        specialty,
        organization_id,
        organization_name,
        patient_city,
        patient_state,

        service_date,
        try_cast(service_date as date) as service_date_casted,
        date_trunc('month', try_cast(service_date as date)) as service_month,

        status_primary,
        status_secondary,
        status_patient,

        claim_outstanding_total,
        latest_outstanding,
        transaction_count,
        total_transaction_amount,
        total_payments,
        total_adjustments,
        total_transfers,
        first_transaction_date,
        last_transaction_date,

        case
            when try_cast(service_date as date) is null then null
            else date_diff('day', try_cast(service_date as date), current_date)
        end as claim_age_days,

        case
            when try_cast(service_date as date) is null then 'unknown'
            when date_diff('day', try_cast(service_date as date), current_date) <= 30 then '0-30 days'
            when date_diff('day', try_cast(service_date as date), current_date) <= 60 then '31-60 days'
            when date_diff('day', try_cast(service_date as date), current_date) <= 90 then '61-90 days'
            else '90+ days'
        end as claim_age_bucket,

        financial_priority_bucket,

        (
            case
                when coalesce(latest_outstanding, 0) > 1000 then 5
                when coalesce(latest_outstanding, 0) > 250 then 3
                else 1
            end
            +
            case
                when transaction_count >= 10 then 3
                when transaction_count >= 5 then 2
                else 0
            end
            +
            case
                when try_cast(service_date as date) is not null
                     and date_diff('day', try_cast(service_date as date), current_date) > 90 then 3
                when try_cast(service_date as date) is not null
                     and date_diff('day', try_cast(service_date as date), current_date) > 60 then 2
                else 0
            end
        ) as priority_score

    from base

)

select *
from final