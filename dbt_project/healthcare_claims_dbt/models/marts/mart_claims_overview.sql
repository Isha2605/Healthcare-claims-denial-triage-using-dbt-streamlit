select
    date_trunc('month', try_cast(service_date as date)) as service_month,

    organization_id,
    organization_name,

    provider_id,
    provider_name,
    specialty,

    status_primary,
    status_secondary,
    status_patient,

    financial_priority_bucket,

    count(*) as claim_count,
    sum(coalesce(claim_outstanding_total, 0)) as total_claim_outstanding,
    avg(coalesce(claim_outstanding_total, 0)) as avg_claim_outstanding,

    sum(coalesce(latest_outstanding, 0)) as total_latest_outstanding,
    avg(coalesce(latest_outstanding, 0)) as avg_latest_outstanding,

    sum(coalesce(total_transaction_amount, 0)) as total_transaction_amount,
    sum(coalesce(total_payments, 0)) as total_payments,
    sum(coalesce(total_adjustments, 0)) as total_adjustments,
    sum(coalesce(total_transfers, 0)) as total_transfers,

    avg(coalesce(transaction_count, 0)) as avg_transaction_count,
    max(coalesce(transaction_count, 0)) as max_transaction_count

from {{ ref('int_claim_enriched') }}
group by
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10